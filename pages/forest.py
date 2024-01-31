import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Forest')

st.markdown('# Forest')

st.sidebar.header("Forest")


st.markdown(
    '''
    Suitable areas for the Nature based projects and biomass calculation using radar data. 

'''
)




st.markdown(
    '''### Case study for the biomass calculation using LIDAR data'''
)

st.markdown(
    '''**The calculation of biomass consists of four primary steps:**

1. Delineate individual tree crowns
2. Calculate predictor variables for all individual trees
3. Collect training data
4. Apply a Random Forest regression model to estimate biomass from the predictor variables'''
)

st.markdown(
    '''Calculations for the sum of biomass'''
)

col1, col2, col3 = st.columns(3)

with col1:
    st.image('calc-biomass_py_25_0.png', caption='Calculation of canopy height')

with col2:
    st.image('tree_crown_cover.png', caption='Calculation of tree crown (area)')

with col3:
    st.image('biomass calculation.png', caption='Biomass distribution in area')


st.markdown('***Sum of biomass is  7249.752  Tonne***')