# 🫀 Task 01 — Heart Disease Dataset Explorer

A Streamlit application built to manually load, process, and explore the **Cleveland Heart Disease Dataset** using Python.

This task focuses on understanding the fundamentals of dataset loading and handling before moving towards statistical analysis and machine learning.

---

## ✨ Features

- 📂 **Manual Dataset Loading**
- 🔗 **Column-to-Value Mapping**
- 🔢 **Numeric Data Conversion**
- ⚠️ **Missing Value Detection**
- 🔃 **Ascending & Descending Sorting**
- 📄 **Pagination**
- 📊 **Rows-per-page Selection**
- 🖥️ **Streamlit Data Explorer**
- 📌 **Dataset & Feature Overview**

---

## 🎯 Task Objective

The objective of this task was to load the Heart Disease dataset into a Streamlit application **without using built-in Pandas dataset-loading functions**.

The application should:

1. Load the dataset manually.
2. Parse the raw `.data` file.
3. Assign meaningful column names to the values.
4. Handle missing values represented by `?`.
5. Convert the values into appropriate numeric types.
6. Display the dataset.
7. Provide sorting options.
8. Provide pagination.

---

## 📊 Dataset

### Cleveland Heart Disease Dataset

| Property | Value |
|---|---:|
| Records | **303** |
| Features | **14** |
| File Format | `.data` |
| Dataset File | `processed.cleveland.data` |

The dataset is stored in the project's root `data` directory:

```text
data/
└── processed.cleveland.data
````

---

## 🧾 Dataset Columns

The dataset contains the following 14 attributes:

| Column       | Description                           |
| ------------ | ------------------------------------- |
| **Age**      | Age of the patient                    |
| **Sex**      | Sex of the patient                    |
| **Cp**       | Chest pain type                       |
| **Trestbps** | Resting blood pressure                |
| **Chol**     | Serum cholesterol                     |
| **Fbs**      | Fasting blood sugar                   |
| **Restecg**  | Resting electrocardiographic results  |
| **Thalach**  | Maximum heart rate achieved           |
| **Exang**    | Exercise-induced angina               |
| **Oldpeak**  | ST depression induced by exercise     |
| **Slope**    | Slope of the peak exercise ST segment |
| **Ca**       | Number of major vessels               |
| **Thal**     | Thalassemia                           |
| **Target**   | Heart disease diagnosis               |

---

## 🧠 How the Dataset is Loaded

The dataset is intentionally loaded **without using `pandas.read_csv()`**.

Each row is manually processed using Python file handling.

### Loading the File

```python
file = open(filename, "r")
```

Each line is then split using the comma delimiter:

```python
values = line.strip().split(",")
```

This produces the individual values contained in each record.

### Column Mapping

The column names are defined separately:

```python
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
```

Each value is connected to its corresponding column name using its index.

For example:

```text
values[0]  → Age
values[1]  → Sex
values[2]  → Cp
values[3]  → Trestbps
...
values[13] → Target
```

The resulting records are stored as dictionaries.

---

## 🔄 Data Processing Flow

The loading process can be summarized as:

```text
Raw Dataset File
       │
       ▼
Read Each Line
       │
       ▼
Split Values Using ","
       │
       ▼
Check for Missing Values
       │
       ├── "?" → None
       │
       └── Valid Value → float()
       │
       ▼
Map Values to Column Names
       │
       ▼
Store Row as Dictionary
       │
       ▼
Add Row to Dataset
       │
       ▼
Streamlit Application
```

---

## ⚠️ Missing Values

The original dataset uses:

```text
?
```

to represent missing values.

During dataset loading, these values are detected and converted to Python:

```python
None
```

For example:

```python
if values[i] == "?":
    row[column_names[i]] = None
```

This prevents missing values from causing errors during numeric conversion.

> Missing-value analysis and handling will be covered separately in a later task.

---

## 🔢 Numeric Conversion

Values that are not missing are converted using:

```python
float(values[i])
```

This allows the application to work with the dataset values numerically and makes operations such as sorting possible.

For example:

```text
"63.0" → 63.0
"145.0" → 145.0
"2.3" → 2.3
```

---

## 🔃 Sorting

The application allows the user to sort the dataset using any available column.

### Sorting Options

* **Ascending**
* **Descending**

For example, sorting by `Age` in ascending order produces:

```text
29
34
34
35
35
37
...
```

Sorting by `Age` in descending order produces:

```text
77
76
74
71
71
70
...
```

The sorting logic also accounts for missing values so that `None` values do not cause comparison errors.

---

## 📄 Pagination

Pagination was implemented to make the dataset easier to explore.

### Rows Per Page

The user can select:

```text
10
20
50
100
```

rows per page.

The application provides:

```text
← Previous          Page 5 of 31          Next →
```

It also displays the current range of records:

```text
Showing rows 41–50 of 303
```

Pagination is implemented using Python list indexing and slicing.

---

## 🖥️ Streamlit Interface

The application provides a simple dataset explorer interface containing:

### Dataset Overview

* Total number of records
* Total number of features

### Display Controls

* Sort By
* Sort Order
* Rows Per Page

### Pagination

* Previous button
* Next button
* Current page
* Total pages
* Displayed row range

### Dataset Preview

The selected records are displayed in a Streamlit data table.

---

## 📸 Application Preview

The application provides a clean interface for exploring the dataset:

```text
┌──────────────────────────────────────────────────────┐
│          🫀 Heart Disease Dataset Explorer           │
│                                                      │
│  Explore the UCI Heart Disease dataset...            │
│                                                      │
│  Records                         Features            │
│  303                             14                  │
│                                                      │
│  ┌────────────── Display Controls ─────────────────┐ │
│  │ Sort By │ Sort Order │ Rows Per Page            │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│                    Pagination                        │
│                                                      │
│       ← Previous    Page 1 of 31    Next →          │
│                                                      │
│                 Dataset Preview                     │
│                                                      │
│  Age │ Sex │ Cp │ Trestbps │ Chol │ Fbs │ ...       │
│  ──────────────────────────────────────────────────  │
│  29  │ 1   │ 2  │ 130      │ 204  │ 0   │ ...      │
│  34  │ 1   │ 1  │ 118      │ 182  │ 0   │ ...      │
└──────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

The overall project is organized by task:

```text
heart-disease-ml/
│
├── data/
│   └── processed.cleveland.data
│
├── task_01_dataset_loading/
│   ├── app.py
│   └── README.md
│
├── task_02_statistics/
│
├── task_03_missing_values/
│
├── reports/
│
├── .gitignore
├── README.md
└── requirements.txt
```

Task 01 contains its own implementation and documentation:

```text
task_01_dataset_loading/
├── app.py
└── README.md
```

---

## 📍 Dataset Path

The application is located inside:

```text
task_01_dataset_loading/
```

while the dataset is stored in:

```text
data/
└── processed.cleveland.data
```

Therefore, the application accesses the dataset using the relative path:

```python
dataset = load_dataset("../data/processed.cleveland.data")
```

The repository structure should be preserved when running the application.

---

## ⚙️ Requirements

The application requires:

* Python 3.x
* Streamlit

All required Python dependencies are listed in the root:

```text
requirements.txt
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/RudraT23/heart-disease-ml.git
```

### 2. Navigate to the Project

```bash
cd heart-disease-ml
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to Task 01

```bash
cd task_01_dataset_loading
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL in the terminal.

Open that URL in a browser to launch the application.

---

## 🧪 Validation

The application was tested for:

* ✅ Dataset loading
* ✅ Correct record count
* ✅ Correct column mapping
* ✅ Missing-value detection
* ✅ Numeric conversion
* ✅ Ascending sorting
* ✅ Descending sorting
* ✅ Rows-per-page selection
* ✅ Previous/Next pagination
* ✅ First page navigation
* ✅ Last page navigation
* ✅ Pagination after sorting
* ✅ Streamlit rendering

The application successfully loads:

```text
303 records
14 features
```

---

## 🛠️ Technologies Used

| Technology    | Purpose                        |
| ------------- | ------------------------------ |
| **Python**    | Dataset loading and processing |
| **Streamlit** | Interactive web interface      |
| **Git**       | Version control                |
| **GitHub**    | Repository and submission      |

---

## 📚 Concepts Practiced

This task focuses on the fundamentals required before moving into statistical analysis and machine learning.

### Python

* File handling
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* String manipulation
* Type conversion
* Sorting
* List slicing

### Data Handling

* Raw dataset parsing
* Delimiter handling
* Column mapping
* Missing-value representation
* Numeric conversion

### Streamlit

* Page layout
* Metrics
* Select boxes
* Buttons
* Containers
* Columns
* Data tables
* Session state
* Application reruns

### Git & GitHub

* Repository initialization
* Commits
* Branch management
* Remote repositories
* Pushing changes to GitHub

---

## 🎯 Learning Outcome

After completing this task, the raw dataset can be loaded and explored programmatically without depending on Pandas' built-in CSV loading functionality.

The implementation provides a foundation for the next stages of the project, where the loaded data can be analyzed statistically and prepared for further machine learning work.

---

## 📌 Task Status

**Task 01 — Completed ✅**

The Cleveland Heart Disease dataset has been manually loaded, parsed, processed, displayed, sorted, and paginated using Python and Streamlit.

---

## 🔗 Repository

[GitHub Repository](https://github.com/RudraT23/heart-disease-ml)

