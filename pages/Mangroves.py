import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Mangroves')

st.markdown('# Mangroves')

st.sidebar.header("Mangroves")

st.markdown('Site selection for the mangrove reforestation is calculated using Multicriteria decision analysis (MCDA) method. Above mentioned variables are used for the decision analysis, some variables are collected from the readily available data while others are extracted from the different datasets such are Global Mangrove Watch (GMW), land use land cover (LULC), etc. The initial area for the analysis taken is the area of mangrove deforestation from year 1996 to the 2020. The abovementioned variables are taken for the site selection. ')

#st.markdown('### Site selection parameters for Mangrove site selection')

st.markdown(
    '''**Site selection parameters for Mangrove site selection:**

1. Tidal range 
2. Recent sea level rise 
3. Projected sea level rise 
4. Recent change in sediments 
5. Time since loss 
6. Average size of loss patches 
7. Proximity of loss areas to remaining mangroves 
8. Distance from human settlement
9. Distance from agricultural areas 
10. Distance from the water source '''
)

