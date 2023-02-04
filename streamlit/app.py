import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go


df_original = pd.read_excel('get_around_delay_analysis.xlsx')
df = pd.read_csv('clean_get_around_delay_analysis.csv')

### Configuration
st.set_page_config(
    page_title="Getaround Dashboard",
    page_icon="📱",
    layout="wide"
)

### App
st.title('Getaround Dashboard')
st.markdown("👋 Welcome on the Getaround Dashboard")
st.sidebar.write('This app is 3 parts:')
st.sidebar.write('1- Exploration 🧭')
st.sidebar.write('2- Data Analysis 📈')
st.sidebar.write('3- Conclusion 💡')

st.subheader('1- Exploration 🧭')




if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_original)

st.subheader('Checkin type for rental')
fig = px.pie(df, values=df['checkin_type'].value_counts(), names=['mobile','connect'])
fig.update_layout(height=500, width=500)                
st.plotly_chart(fig, theme=None, use_container_width=True)

ended = round(len(df[df['state'] == 'ended'])/len(df)*100,2)
st.write(f'{ended} % of rental request are ended')
df_ended = df[df['state'] == 'ended']
df_late = df_ended[df_ended['delay_at_checkout_in_minutes'] > 0]
late_median_time = round(df_late['delay_at_checkout_in_minutes'].median(), 0).astype(int)
st.write(f'The median time for checkout is {late_median_time} minutes after the expected ends for the laters!')

st.subheader('Early and later checkout')
#pie for checkout time
labels = ["Early", "Late under 30 min","Late 60-120 min", "Late more than 180 min", "Late 30-60 min", 'Late 120-180 min']

fig = go.Figure(data=[go.Pie(labels=labels, values=df_ended['checkout'].value_counts(), textinfo='label+percent',
                             insidetextorientation='radial',
                             pull=[0, 0, 0.1, 0.3, 0., 0.2]
                            )])
fig.update(layout_legend=dict(yanchor="top", y=0.6, xanchor="left", x=-1))
st.plotly_chart(fig, theme=None, use_container_width=True)


st.subheader('2- Data Analysis 📈')


st.write('Even if more than fifty percent made ckeckout later , it does not impact the owner, unless the car is rented again:')

st.subheader('Cars rented again, with time for checkout and the checkintype')
#sunburst for cars rented again, with time for checkout and the checkintype
fig = px.sunburst(pd.DataFrame(df.groupby(['rented_again', 'late', 'checkin_type'], as_index=False).size()),
                    path = ['rented_again', 'late', 'checkin_type'],
                    values='size',
                )
fig.update_traces(textinfo="label+percent parent")
fig.update_layout(autosize=False, height=600, width=600)
st.plotly_chart(fig, theme=None, use_container_width=True)

df_rented_again_late = df[(df['rented_again'] == 'rented again') & (df['late'] == 'come later')]
rented_again_late = round(len(df_rented_again_late)/len(df)*100,2)
st.write(f'{rented_again_late} % of rental car are late when the car is rented again')

st.subheader('Cars rented again and come later')
#pie for rented again and come later
labels = ["Late under 30 min", "Late 30-60 min", "Late 60-120 min", "Late more than 180 min", 'Late 120-180 min']

fig = go.Figure(data=[go.Pie(labels=labels, values=df_rented_again_late['checkout'].value_counts(), textinfo='label+percent',
                             insidetextorientation='radial',
                             pull=[ 0, 0, 0, 0.2, 0]
                            )])
fig.update(layout_legend=dict(yanchor="top", y=0.6, xanchor="left", x=-1))
st.plotly_chart(fig, theme=None, use_container_width=True)
rented_again_late180 = round(len(df_rented_again_late[df_rented_again_late['checkout'] == 'Late more than 180 min'])/len(df)*100,2)
st.write(f'{rented_again_late180} % of rental car are late more than 180 min when the car is rented again')



st.subheader('3- Conclusion 💡')


parking = round(len(df[df['rented_again'] == 'Parking'])/len(df)*100, 2)

st.write(f'''After analysis, i recommend after a rental a threshold of 3 hours:

Even though only {rented_again_late180} % are more than 3 hours late, the threshold solves these problematic cases independanting of the checkin type.
For {parking} % of car rental there is no impact by this threshold, their car is not rented again on the same day.

I recommend too to try this threshold and make a new analysis after some weeks, i can refine this threshhold and the scope with more data
like the duration for rental, for example if the rental is 1 hour the threshold should be shorter...
         ''')
