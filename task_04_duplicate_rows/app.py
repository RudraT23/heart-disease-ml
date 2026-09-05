import streamlit as st
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main-title {
    font-size: 3.2rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 0.3rem;
}

.subtitle {
    font-size: 1.05rem;
    color: #9ca3af;
    margin-bottom: 2.5rem;
}

.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 2.5rem;
    margin-bottom: 0.8rem;
}

[data-testid="stMetricLabel"] {
    font-size: 0.9rem;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    font-size: 2rem;
    font-weight: 700;
}

div[data-testid="stAlert"] {
    font-size: 0.95rem;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

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

    with open(filename, "r") as file:
        for line in file:
            values = line.strip().split(",")

            row = {}

            for i, value in enumerate(values):
                if value == "?":
                    row[column_names[i]] = None
                else:
                    row[column_names[i]] = float(value)

            data.append(row)

    return data


def load_test_dataset(filename):
    data = []

    with open(filename, "r") as file:
        lines = file.readlines()

    headers = lines[0].strip().split(",")

    for line in lines[1:]:
        values = line.strip().split(",")

        row = {}

        for i, value in enumerate(values):
            row[headers[i]] = value

        data.append(row)

    return data


def find_duplicate_rows(data):
    duplicates = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                duplicates.append((i, j))

    return duplicates


def remove_duplicate_rows(data):
    unique_rows = []

    for row in data:
        is_duplicate = False

        for unique_row in unique_rows:
            if row == unique_row:
                is_duplicate = True
                break

        if not is_duplicate:
            unique_rows.append(row)

    return unique_rows


dataset = load_dataset("../data/processed.cleveland.data")

duplicates = find_duplicate_rows(dataset)
cleaned_dataset = remove_duplicate_rows(dataset)

validation_dataset = load_test_dataset(
    "test_data/UCI-KNN-1099-11.csv"
)

validation_duplicates = find_duplicate_rows(validation_dataset)
cleaned_validation_dataset = remove_duplicate_rows(
    validation_dataset
)

# Streamlit Interface

st.markdown(
    '<div class="main-title">Heart Disease Duplicate Row Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Detect, validate, and remove duplicate records using a custom '
    'row-comparison algorithm.'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "The Cleveland dataset is the primary dataset for this project. "
    "A second heart disease dataset is used only to validate that "
    "the duplicate detection algorithm works correctly."
)

# Primary Dataset

st.markdown(
    '<div class="section-title">1. Primary Dataset</div>',
    unsafe_allow_html=True
)

st.write(
    f"The Cleveland Heart Disease dataset contains {len(dataset)} "
    "patient records. We first check this dataset for exact duplicate rows."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(dataset))

with col2:
    st.metric("Duplicate Rows", len(duplicates))

with col3:
    st.metric("Rows After Removal", len(cleaned_dataset))

if len(duplicates) == 0:
    st.success("No duplicate rows were found in the Cleveland dataset.")

# Algorithm Validation

st.markdown(
    '<div class="section-title">2. Algorithm Validation</div>',
    unsafe_allow_html=True
)


st.write(
    "Since the primary dataset contains no duplicate rows, "
    "the same custom algorithm is tested on a separate heart "
    "disease dataset containing duplicate records."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Validation Records", len(validation_dataset))

with col2:
    st.metric("Duplicates Detected", len(validation_duplicates))

with col3:
    st.metric("Unique Records", len(cleaned_validation_dataset))

# Duplicate Removal Result

st.markdown(
    '<div class="section-title">3. Duplicate Removal Result</div>',
    unsafe_allow_html=True
)

duplicate_percentage = (
    len(validation_duplicates) /
    len(validation_dataset)
) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Before Cleaning", len(validation_dataset))

with col2:
    st.metric(
        "Duplicates Removed",
        len(validation_dataset) - len(cleaned_validation_dataset)
    )

with col3:
    st.metric("After Cleaning", len(cleaned_validation_dataset))

st.metric(
    "Duplicate Record Percentage",
    f"{duplicate_percentage:.2f}%"
)

# Data Integrity

st.markdown(
    '<div class="section-title">4. Data Integrity Impact</div>',
    unsafe_allow_html=True
)

st.write(
    f"The validation dataset contains "
    f"{len(validation_duplicates)} duplicate records out of "
    f"{len(validation_dataset)} total records. "
    f"After duplicate removal, "
    f"{len(cleaned_validation_dataset)} unique records remain."
)

st.write(
    "Duplicate records reduce the effective amount of unique "
    "information in a dataset. Repeated observations can also "
    "give certain patterns more influence than they should have."
)

# Machine Learning Impact

st.markdown(
    '<div class="section-title">5. Machine Learning Impact</div>',
    unsafe_allow_html=True
)


st.write(
    "Duplicate records can cause a machine learning model to "
    "give disproportionate importance to repeated observations."
)

st.write(
    "If identical records appear in both training and testing "
    "sets, the model may effectively see the same information "
    "during training and evaluation. This can cause data leakage "
    "and lead to overly optimistic evaluation results."
)

st.write(
    "Removing exact duplicate rows before model training helps "
    "ensure that unique observations are represented appropriately."
)
