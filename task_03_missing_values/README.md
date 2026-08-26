# 🩺 Task 03 — Missing Value Identification and Imputation

A Streamlit application for identifying and handling missing values in the **Cleveland Heart Disease Dataset** using manually implemented imputation techniques.

This task focuses on understanding how missing data can be detected, analyzed, and handled without relying on Pandas built-in missing-value functions.

---

## 🎯 Task Objective

The objective of this task is to:

- Identify missing values in the dataset without using `isna()` or `dropna()`.
- Detect the number of missing values in each column.
- Implement multiple imputation techniques manually.
- Compare Mean, Median, and Mode imputation.
- Apply the selected technique to missing values.
- Verify that the missing values have been successfully handled.
- Justify the selected imputation method based on the characteristics of the affected features.

---

## ✨ Features

- 📂 **Manual Dataset Loading**
- 🔍 **Manual Missing Value Detection**
- 📊 **Missing Value Summary**
- ➗ **Manual Mean Calculation**
- 📈 **Manual Median Calculation**
- 🔢 **Manual Mode Calculation**
- 🛠️ **Mean Imputation**
- 🛠️ **Median Imputation**
- 🛠️ **Mode Imputation**
- 🔄 **Before/After Missing Value Verification**
- 🖥️ **Interactive Streamlit Interface**
- 📝 **Detailed Imputation Justification**

---

## 📁 Dataset

The application uses the Cleveland Heart Disease dataset:


data/processed.cleveland.data

The dataset contains:

303 records
14 columns

The columns are:

Age
Sex
Cp
Trestbps
Chol
Fbs
Restecg
Thalach
Exang
Oldpeak
Slope
Ca
Thal
Target

In the original dataset, missing values are represented using:

?

During manual loading, these values are converted to Python:

None

This allows missing values to be detected without using Pandas functions.

##🔍 Missing Values Found

The dataset contains missing values in two columns:

Column	Missing Values
Ca	4
Thal	2

All other columns contain zero missing values.

Therefore, the dataset contains a total of:

6 missing values

## 🧮 Imputation Techniques

Three imputation techniques were implemented manually.

1. Mean Imputation

The missing value is replaced with the arithmetic mean of the available values.

For the affected columns:

Column	Mean
Ca	0.6722
Thal	4.7342

Mean imputation successfully removes the missing values, but it can produce fractional values that are not meaningful for discrete features.

2. Median Imputation

The missing value is replaced with the middle value of the sorted valid values.

Column	Median
Ca	0
Thal	3

Median imputation also successfully removes the missing values.

3. Mode Imputation

The missing value is replaced with the most frequently occurring valid value.

Column	Mode
Ca	0
Thal	3

Mode imputation successfully removes all missing values while preserving actual values already present in the dataset.

## 📊 Method Comparison

The implemented methods produced the following results:

Column	Missing	Mean	Median	Mode
Ca	4	0.6722	0	0
Thal	2	4.7342	3	3

All three techniques were tested and successfully reduced the missing values to zero.

✅ Selected Imputation Method
Mode Imputation

Mode imputation was selected as the final method for the affected columns.

The reason is that both Ca and Thal contain discrete values.

For Ca:

Mean   = 0.6722
Median = 0
Mode   = 0

Ca represents the number of major vessels, so a fractional value such as 0.6722 is not meaningful.

For Thal:

Mean   = 4.7342
Median = 3
Mode   = 3

Thal contains discrete diagnostic categories, so a value such as 4.7342 does not represent an actual category.

Both Median and Mode produce valid values for these columns. Mode was selected because it directly preserves the most frequently occurring value already observed in the dataset.

Final replacement values:

Column	Method	Replacement
Ca	Mode	0
Thal	Mode	3

A detailed comparison and justification is available in REPORT.md.

## 🔄 Verification

The application verifies the number of missing values before and after imputation.

Example:

Ca:
Missing Before → 4
Missing After  → 0

Thal:
Missing Before → 2
Missing After  → 0

This confirms that the implemented imputation process successfully handles the missing values.

The original dataset file is not modified. A freshly loaded copy is used when applying each imputation method.

## 🖥️ Application Interface

The Streamlit application provides:

Total record count
Total missing value count
Missing value summary
Column selection
Imputation method selection
Calculated replacement value
Missing values before imputation
Missing values after imputation
Imputation success confirmation

## 🛠️ Implementation

The task was implemented using Python and Streamlit.

Main Functions
Function	Purpose
load_dataset()	Manually loads and parses the dataset
count_missing_values()	Counts missing values column by column
get_column_values()	Extracts valid values from a column
calculate_mean()	Manually calculates mean
calculate_median()	Manually calculates median
calculate_mode()	Manually calculates mode
impute_missing_values()	Applies the selected imputation method
## 🚫 Constraints Followed

This task was intentionally implemented without using Pandas missing-value functions.

The following were not used:

isna()
dropna()

Missing value detection and imputation were implemented manually using Python lists, dictionaries, loops, conditions, and arithmetic operations.

## 📂 Project Structure
task_03_missing_values/
│
├── app.py
├── README.md
└── REPORT.md

The detailed report is also maintained in the project's central reports directory:

reports/
└── task_03_missing_values_report.md

## ▶️ How to Run

Navigate to the task directory:

cd task_03_missing_values

Run the Streamlit application:

streamlit run app.py

The application will open in the browser.

## 📚 Learning Outcome

This task provided practical understanding of:

Missing data detection
Manual statistical calculations
Mean, median, and mode imputation
Choosing an appropriate imputation strategy
Preserving discrete feature values
Verifying data after preprocessing
Building a simple data preprocessing interface with Streamlit

## 📌 Task Status

Task 03 — Completed ✅

Missing values were identified, multiple imputation techniques were implemented and tested, and Mode Imputation was selected and justified for the affected columns.
