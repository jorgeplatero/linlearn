import streamlit as st
import plotly.graph_objects as go
import numpy as np
import os
from sklearn.datasets import make_classification
import warnings
warnings.filterwarnings('ignore')


#importing css
# -------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'css/style.css')
with open(file_path) as f:
    css = f.read()

#naming the page
# -------------------------------------------------------------
st.set_page_config(
    page_title='About', 
    page_icon='🎓'
)

#explanation
st.write(
    '''
        # About

        This application provides an interactive platform to explore the fundamental concepts of linear 
        classification. By manipulating the model weights (slope and intercept) directly, users can observe 
        the impact of their adjustments on the decision boundary line and model accuracy in real-time.

        **Key Features**

        * Visual exploration: see the linear model line dynamically adjust over the data as you change the 
        weights and bias
        * Accuracy feedback: get real-time insights into the model's performance based on classification 
        accuracy

        **Benefits**

        * Hands-on learning: engage with the concepts of linear models through interactive manipulation
        * Visual understanding: gain a deeper understanding of how model parameters influence the decision 
        boundary and classification results
        * Intuitive interface: the user-friendly design makes it accessible for learners of all levels

        **Target Audience**

        * Students learning about linear classification algorithms
        * Data science enthusiasts looking for a visual and interactive way to explore model parameters
        * Anyone interested in gaining a deeper understanding of how linear models work
    '''
)

#applying css
st.write(f'<style>{css}</style>', unsafe_allow_html=True)