import streamlit as st
column_names = ["Age","Sex","Cp","Trestbps","Chol","Fbs","Restecg","Thalach","Exang","Oldpeak","Slope","Ca","Thal","Target"]

def load_dataset(filename):
    data=[]
    file=open(filename,"r")
    for line in file:
        values=line.strip().split(",")

        row={}

        for i in range(len(values)):
            if values[i]=="?":
                row[column_names[i]] = None
            else:
                row[column_names[i]] = float(values[i])
        data.append(row)
    file.close()
    return data
dataset=load_dataset("../data/processed.cleveland.data")
def sort_dataset(data, column, ascending=True):
    return sorted(
        data,
        key=lambda row: row[column] if row[column] is not None else float("-inf"),
        reverse=not ascending
    )

st.title("Heart Disease Dataset")
st.write("Total Rows:", len(dataset))

sort_column=st.selectbox("Sort By",column_names)
sort_order=st.selectbox("Sort Order",["Ascending","Descending"])
ascending= sort_order == "Ascending"

sorted_data = sort_dataset(dataset,sort_column,ascending)

st.dataframe(sorted_data)