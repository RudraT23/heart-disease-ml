# Task 01: Dataset Loading, Sorting and Pagination
#
# Objective:
# Manually load the UCI Heart Disease dataset without using
# built-in Pandas data-loading functions, and display it
# through a Streamlit application with sorting and pagination.
#
# Dataset: Cleveland Heart Disease Dataset
# Records: 303
# Features: 14
#-----------------------------------------------------------------------------

import streamlit as st
column_names = ["Age","Sex","Cp","Trestbps","Chol","Fbs",
                "Restecg","Thalach","Exang","Oldpeak",
                "Slope","Ca","Thal","Target"]

def load_dataset(filename):
    data=[]
    with open(filename,"r") as file:
        for line in file:
            values=line.strip().split(",")

            row={}

            # Map each value to its corresponding column name.
            # '?' represents a missing value in the original dataset.
            for i in range(len(values)):
                if values[i]=="?":
                    row[column_names[i]] = None
                else:
                    row[column_names[i]] = float(values[i])
            data.append(row)
    return data

def sort_dataset(data, column, ascending=True):
    return sorted(
        data,
        key=lambda row: row[column] if row[column] is not None else float("-inf"),
        reverse=not ascending
    )
dataset=load_dataset("../data/processed.cleveland.data")

st.title("Heart Disease Dataset Explorer")
st.caption("Explore the UCI Heart Disease dataset with manual loading, sorting, and pagination.")
col1, col2 = st.columns(2)

with col1:
    st.metric("Records", len(dataset))

with col2:
    st.metric("Features", len(column_names))

with st.container(border=True):

    st.subheader("Display Controls")

    col1, col2, col3 = st.columns(3)

    with col1:
        sort_column = st.selectbox("Sort By",column_names)
    with col2:
        sort_order = st.selectbox(
            "Sort Order",
            ["Ascending", "Descending"])
    with col3:
        rows_per_page = st.selectbox(
            "Rows Per Page",
            [10, 20, 50, 100])

ascending= sort_order == "Ascending"

sorted_data = sort_dataset(dataset,sort_column,ascending)

total_rows=len(sorted_data)
total_pages=(total_rows+rows_per_page-1)//rows_per_page


if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page > total_pages:
    st.session_state.page = total_pages

page = st.session_state.page

st.subheader("Pagination")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    previous = st.button(
        "← Previous",
        disabled=page == 1,
        use_container_width=True)
with col2:
    st.markdown(
        f"<div style='text-align: center; padding: 8px;'>"
        f"<strong>Page {page} of {total_pages}</strong>"
        f"</div>",unsafe_allow_html=True)
with col3:
    next_page = st.button(
        "Next →",
        disabled=page == total_pages,
        use_container_width=True)
if previous:
    st.session_state.page -= 1
    st.rerun()
if next_page:
    st.session_state.page += 1
    st.rerun()

start_index=(page-1)*rows_per_page
end_index=start_index+rows_per_page

page_data=sorted_data[start_index:end_index]

display_start = start_index + 1
display_end = min(end_index, total_rows)

st.caption(f"Showing rows {display_start}–{display_end} of {total_rows}")

st.subheader("Dataset Preview")
st.dataframe(page_data,
             use_container_width=True,
             hide_index=True)
