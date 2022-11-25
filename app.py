# create a streamlit app to input the ID and print the top 5 labels
import streamlit as st
import pandas as pd

# streamlit app full width
st.set_page_config(layout="wide")

# add logo
st.image("img/tietoevry-logo-digital.webp", width=200)

# title
st.title("Insurance Policy Recommendation System for Existing Customers")

# font size
st.markdown("<style>h1{font-size: 30px;}</style>", unsafe_allow_html=True)

# read the csv file
id_pcode_label = pd.read_csv("data/id_pcode_label.csv")

# create a new dictionary with for unique ID as key, PCODE and Label as values
id_pcode_label_dict = {}

for i in range(len(id_pcode_label)):
    if id_pcode_label['ID'][i] not in id_pcode_label_dict:
        id_pcode_label_dict[id_pcode_label['ID'][i]] = [
            (id_pcode_label['PCODE'][i], id_pcode_label['Label'][i])]
    else:
        id_pcode_label_dict[id_pcode_label['ID'][i]].append(
            (id_pcode_label['PCODE'][i], id_pcode_label['Label'][i]))


# get key from user
key = st.text_input("Enter the ID")

# Add css to make text bigger
st.markdown(
    """
    <style>
        body{
            font-size: 20px;
        }
        div[class*="stTextInput"] label {
        font-size: 26px;
        }
        input {
            font-size: 2rem !important;
        }
        .css-165ax5l {
            width: 50%;
            font-size: 26px;
        }
        .stTextInput{
            width: 50%;
        }
        #T_cc6f8{
            font-size: 2rem !important;
        }
        thead tr th:first-child {
            display:none
        }
        tbody th {
            display:none
        }
        .e16nr0p30{
            font-size: 2rem !important;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# function for given a key, print top 5 values with highest probability except probablity = 1 in a table. And label = 1 in another table format. don't print index.


def top_5_table(key):
    # sort the list of tuples by second element in descending order
    id_pcode_label_dict[key].sort(key=lambda x: x[1], reverse=True)
    # create a new list to store the top 5 values
    top_5_list = []
    # create a new list to store the label = 1 values
    label_1_list = []
    # iterate over the list of tuples
    for i in range(len(id_pcode_label_dict[key])):
        # if the probability is not 1, append the tuple to the list
        if id_pcode_label_dict[key][i][1] != 1:
            top_5_list.append(id_pcode_label_dict[key][i])
        # if the probability is 1, append the tuple to the list
        if id_pcode_label_dict[key][i][1] == 1:
            label_1_list.append(id_pcode_label_dict[key][i])
        # if the length of the list is 5, break the loop
        if len(top_5_list) == 5:
            break
    # create a new dataframe for top 5 values
    top_5_df = pd.DataFrame(top_5_list, columns=['PCODE', 'Label'])
    # create a new dataframe for label = 1 values
    label_1_df = pd.DataFrame(label_1_list, columns=['PCODE', 'Label'])
    # add Table Title
    st.subheader("Existing Insurance Policies")
    # print the label = 1 values in a table format PCODE only. rename PCODE to Insurance Policy Code.
    st.table(label_1_df['PCODE'].rename('Insurance Policy Code'))
    # print the label = 1 values in a table format. and rename the columns PCODE as Insurance Policy Code and Label as Probability. and multiply the probability by 100.
    # st.table(label_1_df.rename(
    #     columns={'PCODE': 'Insurance Policy Code', 'Label': 'Probability'}))
    # add Table Title
    st.subheader("Recommended Insurance Policies")
    # print the top 5 values in a table format. and rename the columns PCODE as Insurance Policy Code and Label as Probability. and multiply the probability by 100.
    st.table(top_5_df.rename(
        columns={'PCODE': 'Insurance Policy Code', 'Label': 'Probability'}).style.format({'Probability': "{:.2%}"}))


# button to print the top 5 values
if st.button('Submit'):
    top_5_table(key)

# for given a key, print top 5 values with highest probability except probablity = 1
# if key:
#     st.write(top_5_table(key))


# add

# hide the text "Made with Streamlit" at the bottom of the page
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
