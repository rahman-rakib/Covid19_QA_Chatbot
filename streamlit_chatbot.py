# import std libraries
import pandas as pd
import time

import streamlit as st
from st_aggrid import AgGrid
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

from chatting import speak
from chatting import answer_fine_tuned
from chatting import answer_base

page = st.sidebar.selectbox("Choose a model", ["Corona Devi", "GPT-3 Curie"]) 

if page == "Corona Devi":
    #  Write title
    st.markdown("# Corona Devi")
    # Put image
    st.image('data/corona_devi.jpg')
    # make columns
    col1,col2 = st.columns([3,1])
    with col1:
        # write subtitle
        st.markdown("#### a covid-19 Q&A chatbot")
    with col2:
        # Write api
        st.write("powered by [GPT-3](https://openai.com/blog/gpt-3-apps/)")

    #############################################################################
    # Fine-tuned model
    #############################################################################

    st.markdown("""
    #
    ### Ask Corona Devi
    """)

    # Write inside a form
    with st.form(key="corona_devi"):
        # query input
        query = st.text_input(label="write here")
        # space
        st.write("") 

        # create columns 
        col1,col2,col3,col4,col5 = st.columns([1,5,2,5,1])
        
        with col2:
            # temperature input
            temp_val = st.slider("creativity",value=10)
            # submit button
            submit_button = st.form_submit_button(label="submit")
        
        with col4:
            # max_token input
            token_val = st.slider("verbosity",value=25)
            # audio_output checkbox
            talkativeness = st.checkbox("audio")
        
        # customized values
        temp_ = round(temp_val/100,2)
        token_ = int(token_val*2.56)

        # give output
        if submit_button:
            with st.spinner(text="reaching Corona Devi"):
                answer_ = answer_fine_tuned(query,temp=temp_,token=token_)
            st.write("") 
            st.write(answer_)
            if talkativeness:
                with st.spinner(text="Corona Devi speaking"):
                    time.sleep(1)
                    speak(answer_)

else: 
    #  Write title
    st.markdown("# GPT-3 Curie")
    # Put image
    st.image('data/GPT3.jpg')
    # make subtitle
    st.markdown("#### a GPT-3 language model")
    
    #############################################################################
    # Base GPT-3 model: Curie
    #############################################################################

    st.markdown("""
    #
    ### Ask Curie
    """)

    # Write inside a form
    with st.form(key="curie_the_primal"):
        # query input
        query = st.text_input(label="write here")
        # space
        st.write("")

        # make columns
        col1,col2,col3,col4,col5 = st.columns([1,5,2,5,1])
        
        with col2:
            # temperature input
            temp_val_b = st.slider("creativity",value=10)
            # submit button
            submit_button_b = st.form_submit_button(label="submit")
            
        with col4:
            # max_token input
            token_val_b = st.slider("verbosity",value=25)
            # audio_output checkbox
            talkativeness_b = st.checkbox("audio")

        # customized values
        temp_ = round(temp_val_b/100,2)
        token_ = int(token_val_b*2.56)
        
        # give output
        if submit_button_b:
            with st.spinner(text="reaching Curie"):
                answer_ = answer_base(query,temp=temp_,token=token_)
            st.write("") 
            st.write(answer_)
            if talkativeness_b:
                with st.spinner(text="Curie speaking"):
                    time.sleep(1)
                    speak(answer_)
