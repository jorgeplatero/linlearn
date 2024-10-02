import streamlit as st
import numpy as np
import os
from sklearn.datasets import make_classification
import warnings
warnings.filterwarnings('ignore')


#importing css
# -------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '../css/style.css')
with open(file_path) as f:
    css = f.read()

#naming the page
# -------------------------------------------------------------
st.set_page_config(
    page_title='Background', 
    page_icon='🎓'
)

#explanation
st.write(
    '''
        # Linear Classification

        In this app we'll refresh your memory about linear equations while also helping you see a line as 
        a linear classifier. Here we take the first steps towards undertanding complex AI models such as neural 
        networks.

        ## Linear Equation

        The linear equation is learned in the form $ax + by + c$, but to adapt to neural network terminology, 
        we can rewrite this equation as ${f{w_1x_1 + w_2x_2 + b}}$. That is, $f{w_1}$, $bf{w_2}$ and $bf{b}$ 
        are the parameters that define our linear model, our line. Let's start by plotting a specific line: 
        $f{-1x_1 + 4x_2 + 0.4}$
    '''
)
_, col2, _ = st.columns([.2, .6, .2])
with col2:
    st.image('img/plot1.png', use_column_width=True)
st.write(
    '''
        **Solving the liner equation for different points**

        Next we'll select three points in space and solve the equation of the line for these points. 
    '''
)
_, col2, _ = st.columns([.2, .6, .2])
with col2:
    st.image('img/plot2.png', use_column_width=True)
st.write(
    '''
        Note that point :red[$p_1$] is on the line, while :blue[$p_2$] is above the line and :green[$p_3$] is 
        below. When solving the equation of the line for these three points, we obtained respectively zero 
        $(=0)$, positive $(>0)$ and negative $(<0)$ results.

        This behavior is consistent for any points on the line, above or below it. In other words, if we call
        linear equation $f(x)$, we have the following rules:
        - $f(x) = 0$ defines points on the line
        - $f(x) > 0$ defines points above the line
        - $f(x) < 0$ defines points below the line

        ## Linear Model

        Our line can be interpreted as a linear model, which is nothing more than a **mapping function**
        $X -> Y$, which maps each point in $X$ to a point in $Y$. In other words, given the parameters 
        $W = \{w_1, w_2\}$ and $b$ of a line, it is possible to map an input $X = \{x_1, x_2\}$ to the output
        $f(x; W, b)$.

        For classification problems, the values of $y$ for new inputs $x$ will determine whether $x$ is a 
        point above or below the line, thus forming a classifier capable of **linearly separating problems 
        with two classes**.

        ### General Rule

        Formalizing neural network terminology, in two dimensions $(x_1, x_2)$ our linear model has two 
        **weights** $(w_1, w_2)$ and a **bias** $b$. 

        In two dimensions our model forms a line, as we saw earlier. For a number of dimensions $d > 2$, linear
        models are called **hyperplanes**, and are composed of:
        - a weight $w_i$ for each dimension $x_i$
        - a single bias $b$

        For example, for 3 dimensions $(x_1, x_2, x_3)$ we would have three weights $(w_1, w_2, w_3)$ and a 
        single bias $b$.Its mapping function would be $y = w_1x_1 + w_2x_2 + w_3x_3 + b$

        In general, it is defined that given an input with $d$ dimensions, the mapping function of ablinear 
        model is

        $y = \sum^{d}_{i=1}w_ix_i + b$
    '''
)

#applying css
st.write(f'<style>{css}</style>', unsafe_allow_html=True)