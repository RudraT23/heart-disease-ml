# Task 04 — Duplicate Row Detection and Removal

## Overview

This task focuses on detecting and removing duplicate rows from a heart disease dataset using a custom row-comparison algorithm.

The implementation is intentionally built without using built-in duplicate detection or removal functions such as `pandas.DataFrame.duplicated()` or `drop_duplicates()`.

The task also examines how duplicate records can affect data integrity and machine learning workflows.

---

## Objectives

- Check the primary dataset for duplicate rows.
- Implement a custom duplicate comparison algorithm.
- Manually remove duplicate rows.
- Validate the algorithm using a separate dataset containing duplicate records.
- Analyze the effect of duplicate records on data integrity.
- Understand the potential impact of duplicates on machine learning models.

---

## Datasets

### Primary Dataset

**Cleveland Heart Disease Dataset**

The Cleveland dataset is the primary dataset used throughout this project.

It contains:

- **303 records**
- **14 columns**

The custom duplicate detection algorithm was applied to the complete dataset.

Result:

```text
Total Records: 303
Duplicate Rows: 0
Rows Removed: 0

No exact duplicate rows were found.

Validation Dataset

UCI-KNN-1099-11.csv

A separate heart disease dataset is included in the test_data directory to validate the duplicate detection and removal implementation.

This dataset is used only for algorithm validation. It does not replace the primary Cleveland dataset.

Result:

Total Records: 1099
Duplicate Rows: 181
Rows After Removal: 918
Rows Removed: 181
Implementation
Duplicate Detection

The duplicate detection algorithm compares every row with subsequent rows in the dataset.

When two complete rows contain identical values, the later row is recorded as a duplicate.

The implementation uses nested loops and direct row comparison.

Duplicate Removal

The removal algorithm creates a new dataset containing only unique rows.

Each incoming row is compared against the rows already accepted into the cleaned dataset. If an identical row already exists, the row is skipped.

Results
Dataset	Original Records	Duplicate Rows	Records After Cleaning	Rows Removed
Cleveland	303	0	303	0
UCI-KNN Validation	1,099	181	918	181

The validation dataset contained approximately 16.47% duplicate records.

Data Integrity

Duplicate records reduce the amount of unique information represented in a dataset.

Repeated observations can give certain records more influence than intended and may distort the representation of the underlying data.

Removing exact duplicate rows produces a dataset containing unique observations and improves the structural quality of the data.

Machine Learning Impact

Duplicate observations can influence machine learning models by giving repeated records disproportionate influence during training.

Duplicates can also cause data leakage when identical observations appear in both training and testing datasets. This can result in overly optimistic evaluation results because the test set is no longer completely independent of the training data.

Removing duplicates before model training helps reduce these risks and provides a cleaner dataset for subsequent machine learning workflows.

How to Run

Navigate to the task directory:

cd task_04_duplicate_rows

Run the Streamlit application:

streamlit run app.py

The application displays:

Primary Cleveland dataset results
Duplicate detection validation results
Before and after cleaning statistics
Data integrity analysis
Machine learning impact analysis
Project Structure
task_04_duplicate_rows/
│
├── app.py
├── README.md
├── REPORT.md
│
└── test_data/
    └── UCI-KNN-1099-11.csv
Key Learning

This task demonstrates how duplicate records can be detected and removed without relying on high-level data-processing libraries.

It also demonstrates the importance of checking data quality before using a dataset for machine learning.

The validation experiment confirms that the custom duplicate detection and removal functions operate on the supplied data rather than relying on a hardcoded duplicate count.