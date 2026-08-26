import streamlit as st

column_names = [
    "Age",
    "Sex",
    "Cp",
    "Trestbps",
    "Chol",
    "Fbs",
    "Restecg",
    "Thalach",
    "Exang",
    "Oldpeak",
    "Slope",
    "Ca",
    "Thal",
    "Target"
]

def load_dataset(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            row = {}

            for i in range(len(values)):
                if values[i] == "?":
                    row[column_names[i]] = None
                else:
                    row[column_names[i]] = float(values[i])
            data.append(row)
    return data

def count_missing_values(data):
    missing_counts = {}

    for column in column_names:
        count = 0

        for row in data:
            if row[column] is None:
                count += 1

        missing_counts[column] = count

    return missing_counts

def get_column_values(data,column):
    values = []

    for row in data:
        if row[column] is not None:
            values.append(row[column])

    return values

def calculate_mean(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)

def calculate_median(values):
    sorted_values = sorted(values)

    n = len(sorted_values)
    middle = n // 2

    if n % 2 == 1:
        return sorted_values[middle]
    return (sorted_values[middle - 1] + sorted_values[middle]) / 2

def calculate_mode(values):
    frequency = {}
    for value in values:
        if value not in frequency:
            frequency[value] = 1
        else:
            frequency[value] += 1
    mode = None
    highest_frequency =0

    for value in frequency:
        if frequency[value] > highest_frequency:
            highest_frequency =  frequency[value]
            mode = value

    return mode

def impute_missing_values(data, column, method):
    values = get_column_values(data, column)

    if method == "Mean":
        replacement = calculate_mean(values)

    elif method == "Median":
        replacement = calculate_median(values)

    elif method == "Mode":
        replacement = calculate_mode(values)

    for row in data:
        if row[column] is None:
            row[column] = replacement

    return data

dataset = load_dataset("../data/processed.cleveland.data")

missing_values = count_missing_values(dataset)

st.title("Heart Disease Missing Value Explorer")

st.caption(
    "Identify and manually impute missing values from the Cleveland Heart Disease dataset."
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Records", len(dataset))

with col2:
    total_missing = 0

    for count in missing_values.values():
        total_missing += count

    st.metric("Missing Values", total_missing)


st.subheader("Missing Value Summary")

for column in missing_values:
    if missing_values[column] > 0:
        st.write(f"**{column}:** {missing_values[column]} missing values")


st.subheader("Imputation")

column = st.selectbox(
    "Select Column",
    ["Ca", "Thal"]
)

method = st.selectbox(
    "Select Imputation Method",
    ["Mean", "Median", "Mode"]
)

values = get_column_values(dataset, column)

if method == "Mean":
    replacement = calculate_mean(values)

elif method == "Median":
    replacement = calculate_median(values)

else:
    replacement = calculate_mode(values)

missing_before = missing_values[column]

st.write(f"**Replacement Value:** {replacement:.2f}")
st.write(f"**Missing Values Before:** {missing_before}")

if st.button("Apply Imputation", use_container_width=True):

    imputed_data = load_dataset("../data/processed.cleveland.data")

    imputed_data = impute_missing_values(
        imputed_data,
        column,
        method
    )

    remaining_missing = 0

    for row in imputed_data:
        if row[column] is None:
            remaining_missing += 1

    st.success("Imputation completed successfully.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Missing Before", missing_before)

    with col2:
        st.metric("Missing After", remaining_missing)