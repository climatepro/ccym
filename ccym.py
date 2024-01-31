import streamlit as st
import pandas as pd


st.set_page_config(page_title='CCYM Carbon Capture Yield Model')

st.markdown('# CCYM Carbon Capture Yield Model')

st.sidebar.header("CCYM vericals")


st.markdown(
    '''The carbon credit model estimates the carbon emissions sources and carbon sinks on a particular area. The existing land use and future land use is considered to calculate the projection of the carbon emissions and carbon sinks.  

Land use determines the carbon status with forests sequestering carbon, whereas urban areas are carbon emission sources. Certain land uses can be both emissions sources and sinks such as forest land that is degraded.'''
)

st.markdown('## CCYM project verticals')

st.markdown('* **Mangrove**')

st.markdown('* **Forest**')

st.markdown('* **Biochar**')

st.markdown('* **Solar**')