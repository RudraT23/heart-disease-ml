
# 📊 Task 02 — Heart Disease Summary Statistics

A Streamlit application that calculates and displays summary statistics for the Cleveland Heart Disease Dataset using **manual Python implementations**.

This task focuses on understanding the fundamental statistical calculations behind common descriptive statistics without relying on built-in statistical functions.

---

## 🎯 Task Objective

The objective of this task was to calculate the following summary statistics manually:

- Mean
- Median
- Mode
- Minimum
- Maximum
- Standard Deviation

The calculations were implemented using basic Python logic instead of built-in statistical functions or Pandas statistical methods.

---

## ✨ Features

- 📂 Manual dataset loading
- 🔢 Numeric value extraction
- 📊 Manual calculation of summary statistics
- 📈 Mean calculation
- 📍 Median calculation
- 🔁 Mode calculation
- ⬇️ Minimum calculation
- ⬆️ Maximum calculation
- 📐 Standard deviation calculation
- 🖥️ Streamlit interface
- 🔽 Feature selection
- ⚠️ Missing-value handling

---

## 📊 Dataset

### Cleveland Heart Disease Dataset

| Property | Value |
|---|---:|
| Records | **303** |
| Original Features | **14** |
| File Format | `.data` |
| Dataset File | `processed.cleveland.data` |

The dataset is stored in the project's root `data` directory:

```text
data/
└── processed.cleveland.data
````

---

## 🧾 Dataset Columns

The original dataset contains the following 14 columns:

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

## 🔢 Features Used for Statistics

Summary statistics are calculated for the following numerical measurements:

```text
Age
Trestbps
Chol
Thalach
Oldpeak
```

These columns represent continuous numerical measurements for which statistics such as mean, median, minimum, maximum, and standard deviation are directly meaningful.

Encoded categorical or target columns are not included in the feature selector.

---

## 🧠 Manual Statistical Calculations

The main requirement of this task was to implement the statistical calculations manually.

No functions such as:

```python
statistics.mean()
statistics.median()
statistics.mode()
statistics.stdev()
```

were used.

Pandas statistical functions were also not used.

---

## 📈 Mean

The mean is calculated by adding all values and dividing the total by the number of values.

Formula:

```text
Mean = Sum of all values / Number of values
```

Implementation:

```python
def calculate_mean(values):
    total = 0

    for value in values:
        total += value

    return total / len(values)
```

---

## 📍 Median

The median is the middle value after sorting the dataset.

For an odd number of values:

```text
Median = Middle value
```

For an even number of values:

```text
Median = (Middle value 1 + Middle value 2) / 2
```

Implementation:

```python
def calculate_median(values):
    sorted_values = sorted(values)

    n = len(sorted_values)
    middle = n // 2

    if n % 2 == 1:
        return sorted_values[middle]

    return (sorted_values[middle - 1] + sorted_values[middle]) / 2
```

---

## 🔁 Mode

The mode is the value that occurs most frequently.

A dictionary is used to manually count the frequency of each value.

```python
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
```

If multiple values have the same highest frequency, the current implementation returns the first value encountered with that frequency.

---

## ⬇️ Minimum

The minimum value is found by comparing every value with the current minimum.

```python
def calculate_min(values):
    minimum = values[0]

    for value in values:
        if value < minimum:
            minimum = value

    return minimum
```

---

## ⬆️ Maximum

The maximum value is found by comparing every value with the current maximum.

```python
def calculate_max(values):
    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value

    return maximum
```

---

## 📐 Standard Deviation

The application calculates **sample standard deviation**.

The process is:

1. Calculate the mean.
2. Find the difference between each value and the mean.
3. Square each difference.
4. Add the squared differences.
5. Divide by `n - 1` to obtain the sample variance.
6. Take the square root of the variance.

Formula:

```text
Sample Variance = Σ(x - mean)² / (n - 1)

Sample Standard Deviation = √Sample Variance
```

Implementation:

```python
def calculate_std(values):
    mean = calculate_mean(values)

    squared_difference_total = 0

    for value in values:
        difference = value - mean
        squared_difference_total += difference ** 2

    variance = squared_difference_total / (len(values) - 1)

    return variance ** 0.5
```

Using `n - 1` means the calculation represents **sample standard deviation** rather than population standard deviation.

---

## 🧩 Statistics Calculation Flow

The application processes a selected feature using the following flow:

```text
Dataset
   │
   ▼
Select Numerical Feature
   │
   ▼
Extract Valid Values
   │
   ▼
Manual Calculations
   │
   ├── Mean
   ├── Median
   ├── Mode
   ├── Minimum
   ├── Maximum
   └── Standard Deviation
   │
   ▼
Display Results in Streamlit
```

---

## 🖥️ Streamlit Interface

The application provides a simple interface where the user can select one of the supported numerical features.

### Available Features

```text
Age
Trestbps
Chol
Thalach
Oldpeak
```

After selecting a feature, the application displays:

```text
Mean
Median
Mode
Minimum
Maximum
Standard Deviation
```

All values are calculated dynamically for the selected feature.

---

## 📸 Application Preview

The interface contains:

```text
┌──────────────────────────────────────────────┐
│       Heart Disease Summary Statistics      │
│                                              │
│ Explore manually calculated statistics...   │
│                                              │
│ Select Feature                               │
│ [ Age                                  ▼ ]   │
│                                              │
│ Statistics for Age                           │
│                                              │
│ Mean        Median        Mode               │
│ 54.44       56.00         58.00              │
│                                              │
│ Minimum     Maximum       Standard Deviation │
│ 29.00       77.00         9.04               │
└──────────────────────────────────────────────┘
```

---

## ⚠️ Missing Values

The dataset uses:

```text
?
```

to represent missing values.

During dataset loading, these values are converted to:

```python
None
```

Only valid values are included when calculating the summary statistics.

For example:

```python
def get_column_values(data, column):
    values = []

    for row in data:
        if row[column] is not None:
            values.append(row[column])

    return values
```

This prevents missing values from interfering with the calculations.

---

## 📁 Project Structure

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
├── task_02_summary_statistics/
│   ├── app.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

## 📍 Dataset Path

Task 02 is located inside:

```text
task_02_summary_statistics/
```

The dataset is located in:

```text
data/
└── processed.cleveland.data
```

Therefore, the application accesses the dataset using:

```python
dataset = load_dataset("../data/processed.cleveland.data")
```

The repository structure should be preserved when running the application.

---

## ⚙️ Requirements

The application requires:

* Python 3.x
* Streamlit

Dependencies are listed in:

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

### 4. Navigate to Task 02

```bash
cd task_02_summary_statistics
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL in the terminal.

Open the URL in a browser to launch the application.

---

## 🧪 Validation

The application was tested using all supported numerical features:

* ✅ Age
* ✅ Trestbps
* ✅ Chol
* ✅ Thalach
* ✅ Oldpeak

The calculations were also tested independently before being connected to the Streamlit interface.

The application was verified for:

* ✅ Correct dataset loading
* ✅ Correct record count
* ✅ Missing-value handling
* ✅ Manual mean calculation
* ✅ Manual median calculation
* ✅ Manual mode calculation
* ✅ Manual minimum calculation
* ✅ Manual maximum calculation
* ✅ Manual standard deviation calculation
* ✅ Feature selection
* ✅ Dynamic statistics updates
* ✅ Streamlit rendering

---

## 🛠️ Technologies Used

| Technology    | Purpose                                      |
| ------------- | -------------------------------------------- |
| **Python**    | Dataset loading and statistical calculations |
| **Streamlit** | Interactive user interface                   |
| **Git**       | Version control                              |
| **GitHub**    | Repository and submission                    |

---

## 📚 Concepts Practiced

### Python

* File handling
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* Sorting
* Type conversion
* Dictionary frequency counting

### Statistics

* Mean
* Median
* Mode
* Minimum
* Maximum
* Variance
* Standard deviation

### Streamlit

* Page titles
* Captions
* Select boxes
* Columns
* Metrics
* Dynamic UI updates

---

## 🎯 Learning Outcome

This task provided practical understanding of how common descriptive statistics are calculated internally rather than relying on ready-made statistical functions.

The implementation also demonstrates how manually calculated results can be connected to an interactive Streamlit interface.

---

## 📌 Task Status

**Task 02 — Completed ✅**

The Cleveland Heart Disease dataset is loaded manually and the required summary statistics are calculated without using built-in statistical functions.

The results can be explored interactively through the Streamlit application.

