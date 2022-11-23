# create a streamlit app to input the ID and print the top 5 labels
import streamlit as st
import pandas as pd


# load the data withoout the index
data = pd.read_csv('data/id_pcode_top5.csv')


# multiply 100 to label column
data['Label'] = data['Label'] * 100

# dount display the index
print(data.set_index('ID'))