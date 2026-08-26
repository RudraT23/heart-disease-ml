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
# Columns suitable for numerical summary statistics
numeric_columns = [
    "Age",
    "Trestbps",
    "Chol",
    "Thalach",
    "Oldpeak"
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

def get_column_values(data, column):
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
    highest_frequency = 0

    for value in frequency:
        if frequency[value] > highest_frequency:
            highest_frequency = frequency[value]
            mode = value
    return mode

def calculate_min(values):

    minimum = values[0]
    for value in values:
        if value < minimum:
            minimum = value

    return minimum

def calculate_max(values):
    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value
    return maximum

def calculate_std(values):
    mean = calculate_mean(values)

    squared_difference_total = 0

    for value in values:
        difference = value - mean
        squared_difference_total += difference ** 2

    variance = squared_difference_total / (len(values) - 1)
    return variance ** 0.5

def calculate_statistics(values):
    return {
        "Mean": calculate_mean(values),
        "Median": calculate_median(values),
        "Mode": calculate_mode(values),
        "Minimum": calculate_min(values),
        "Maximum": calculate_max(values),
        "Standard Deviation": calculate_std(values)
    }

dataset = load_dataset("../data/processed.cleveland.data")


st.title("Heart Disease Summary Statistics")

st.caption(
    "Explore manually calculated statistics from the Cleveland Heart Disease dataset."
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Records", len(dataset))

with col2:
    st.metric("Numeric Features", len(numeric_columns))

with st.container(border=True):
    st.subheader("Statistics Controls")

    selected_column = st.selectbox(
        "Select Feature",
        numeric_columns
    )

values = get_column_values(dataset, selected_column)
statistics = calculate_statistics(values)

st.subheader(f"Statistics for {selected_column}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Mean",
        f"{statistics['Mean']:.2f}"
    )

with col2:
    st.metric(
        "Median",
        f"{statistics['Median']:.2f}"
    )

with col3:
    st.metric(
        "Mode",
        f"{statistics['Mode']:.2f}"
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Minimum",
        f"{statistics['Minimum']:.2f}"
    )

with col2:
    st.metric(
        "Maximum",
        f"{statistics['Maximum']:.2f}"
    )

with col3:
    st.metric(
        "Standard Deviation",
        f"{statistics['Standard Deviation']:.2f}"
    )


st.caption(
    f"{selected_column} contains {len(values)} valid values, "
    f"ranging from {statistics['Minimum']:.2f} "
    f"to {statistics['Maximum']:.2f}."
)
