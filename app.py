# create a streamlit app to input the ID and print the top 5 labels
import streamlit as st
import pandas as pd


# load the data withoout the index
data = pd.read_csv('data/id_pcode_top5.csv')


# multiply 100 to label column
data['Label'] = data['Label'] * 100



# ## input the ID and print the top 5 labels
# input_id = input("Enter ID: ")
# id_pcode_top5_read.loc[id_pcode_top5_read['ID'] == str(input_id)]

# title
st.title('Insurance Plan Recommendation System for Existing Customers.')

# get the Existing Customer ID
input_id = st.text_input("Enter Policy Holder ID: ")


# button to submit the ID
if st.button('Submit'):
    # display PCODE and Label columns as Policy Code and Probability. 
    st.write(data.loc[data['ID'] == str(input_id)][['PCODE', 'Label']].rename(columns={'PCODE': 'Policy Code', 'Label': 'Probability'}))
    # st.write(data.loc[data['ID'] == str(input_id)][['PCODE', 'Label']])

## comment out the streamlit app and run the code in the terminal