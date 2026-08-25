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

st.title("Heart Disease Dataset")
st.write("Total Rows:", len(dataset))
st.dataframe(dataset)