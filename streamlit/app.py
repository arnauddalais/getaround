import streamlit as st
import requests
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import seaborn as sns
import numpy as np
import json
import re

df = pd.read_excel('get_around_delay_analysis.xlsx')

### Configuration
st.set_page_config(
    page_title="Getaround Dashboard",
    page_icon="📱",
    layout="wide"
)

### App
st.title('Getaround Dashboard')
st.markdown("👋 Welcome on the Getaround Dashboard")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

