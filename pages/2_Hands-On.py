import streamlit as st
import plotly.graph_objects as go
import numpy as np
import os
from sklearn.datasets import make_classification
import warnings
warnings.filterwarnings('ignore')


#functions
def play_fig(w1, w2, b, X, Y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=X[:, 0],
        y=X[:, 1],
        mode='markers',
        marker=dict(
            color=['#90d6ff' if y == 0 else '#ff474c' for y in Y],
            size=10
        ),
        hovertemplate='X: %{x:.2f}<br>Y: %{y:.2f}<extra></extra>'
    ))
    xmin = X[:, 0].min() - 1 
    xmax = X[:, 0].max() + 1  
    ymin = X[:, 1].min() - 1  
    ymax = X[:, 1].max() + 1
    x = np.linspace(xmin, xmax, 50)
    y = (-w1 * x - b) / w2
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        line=dict(color='#31333f', width=1.5)
    ))
    fig.add_trace(go.Scatter(
        x=[xmin, xmax],
        y=[0, 0],
        mode='lines',
        line=dict(color='#31333f', width=1, dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=[0, 0],
        y=[ymin, ymax],
        mode='lines',
        line=dict(color='#31333f', width=1, dash='dash')
    ))
    fig.update_layout(
        title='',
        xaxis_range=[xmin, xmax],
        yaxis_range=[ymin, ymax],
        plot_bgcolor='#586e75',
        showlegend=False,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_title='X',
        yaxis_title='Y',
        height=400,
        margin=dict(l=0, r=0, b=0, t=0, pad=0)
    )
    st.plotly_chart(fig, use_container_width=True)


def classify(ponto, w1, w2, b):
    ret = w1 * ponto[0] + w2 * ponto[1] + b
    if ret >= 0:
        return 1, 'yellow'
    else:
        return 0, 'blue'


#importing css
# -------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '../css/style.css')
with open(file_path) as f:
    css = f.read()

#naming the page
# -------------------------------------------------------------
st.set_page_config(
    page_title='Playground', 
    page_icon='img/ico.ico'
)

#title
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('LinLearn | Hands-On')

#importing random data
np.random.seed(46)
X, Y = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)

#requesting user data
st.write(
    '''
        ## Let's play!?

        We're going to train a linear classifier in two dimensions using the most advanced technology available: 
        **your brain!** Your job is to find the best parameters $(W, b)$ of a linear model to classify 
        the generated distribution.
    '''
)
col1, col2, col3, col4 = st.columns(4)
with col1:
    w1 = st.number_input('**$w_1$**', value=-0.33, step=0.1, help='Optimal value: 5', format='%0.2f')
with col2:
    w2 = st.number_input('**$w_2$**', value=0.09, step=0.1, help='Optimal value: 1,85', format='%0.2f')
with col3:
    b = st.number_input('**$b$**', value=-0.26, step=0.1, help='Optimal value: -0,7', format='%0.2f')
with col4:
    acertos = 0
    for k in range(len(X)):
        categ, _ = classify(X[k], w1, w2, b)
        if categ == Y[k]:
            acertos += 1
    st.metric('**Accuracy**', f'{acertos/len(X)*100:.2f}%')
    
#figure
play_fig(w1, w2, b, X, Y)
st.write(
    '''
        The graph above produces a random distribution for a two-class classification problem, 
        represented by points generated with the ```make_classification()``` function of sklearn. 
        Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html
    '''
)

#applying css
st.write(f'<style>{css}</style>', unsafe_allow_html=True)