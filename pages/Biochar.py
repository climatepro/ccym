import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Biochar')

st.markdown('# Biochar')

st.sidebar.header("Biochar")

st.markdown(
    '''Selecting the site for biochar plant that can process the agricutural waste. Site selection is applied to the State of **Tamil Nadu**.

'''
)

st.markdown('### Key factors considered for the site selection are:')

st.markdown('* **Agricultural productivity**')
st.markdown('* **Crop residue buring**')
st.markdown('* **River basin visinity**')
st.markdown('* **Total Cultivated area**')
st.markdown('* **Crop residue/waste generation**')

st.write('---')


st.markdown('### Tamil Nadu agricutural productivity')
st.image('prod_per_dist.png', caption='Area normallized crop production per district for Tamil Nadu')
st.write('---')


st.markdown('### Stubble burning over Tamil Nadu')
st.image('monthly_fires_tamil_nadu.png', caption='Monthly crop fire recordings by VIIRS satellite for 10 years over Tamil Nadu')
st.write('---')


st.markdown('### Site selection for Biochar')
st.markdown('Hotspot analysis is done for Tamil Nadu to find high production and stubble burning instances of selected crops. For each clusters collected some potential locations by considering avaiablity of nearby industries, transportation, river basin.')
st.image('site_selection_clusters.png', caption='Highly suitable clusters for site selection over Tamil Nadu')
st.write('---')
