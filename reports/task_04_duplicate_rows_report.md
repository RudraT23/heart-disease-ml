# Task 04 — Duplicate Row Detection and Removal

## Objective

The objective of this task is to identify duplicate rows in a heart disease dataset using a custom row-comparison algorithm, remove duplicate records manually, and analyze the effect of duplicate data on data integrity and machine learning models.

The implementation does not use built-in duplicate-removal functions such as `drop_duplicates()`.

---

## Dataset

The primary dataset used in this project is the Cleveland Heart Disease dataset.

It contains 303 patient records and 14 columns representing patient characteristics and the heart disease target.

The primary dataset was checked for exact duplicate rows using the custom comparison algorithm.

### Primary Dataset Result

| Metric | Result |
|---|---:|
| Total Records | 303 |
| Duplicate Rows | 0 |
| Rows After Removal | 303 |
| Rows Removed | 0 |

No exact duplicate rows were found in the Cleveland dataset.

---

## Algorithm Validation

Since the primary Cleveland dataset did not contain duplicate rows, a separate heart disease dataset, `UCI-KNN-1099-11.csv`, was used to validate the duplicate detection and removal functions.

This dataset was used only as a validation dataset. The Cleveland dataset remains the primary dataset for the project.

The same custom functions were applied to the validation dataset without hardcoding the expected duplicate count.

### Validation Result

| Metric | Result |
|---|---:|
| Original Records | 1,099 |
| Duplicate Rows Detected | 181 |
| Rows After Removal | 918 |
| Rows Removed | 181 |
| Duplicate Percentage | 16.47% |

The algorithm successfully detected 181 duplicate row occurrences and removed them, leaving 918 unique records.

---

## Methodology

### Duplicate Detection

The duplicate detection algorithm compares each row with the rows that appear after it in the dataset.

For every pair of rows:

1. Select the current row.
2. Compare it with every subsequent row.
3. If both rows contain the same values, the later row is recorded as a duplicate.
4. Continue until all row combinations have been checked.

This approach avoids using a built-in duplicate detection function and demonstrates the comparison logic directly.

### Duplicate Removal

A separate manual removal function builds a new list containing only unique rows.

For each row:

1. Compare it with the rows already stored as unique.
2. If an identical row already exists, mark it as a duplicate.
3. Otherwise, add the row to the unique dataset.

The resulting dataset contains only unique records.

---

## Data Integrity Impact

Duplicate records reduce the amount of unique information represented in a dataset.

In the validation dataset, 181 duplicate row occurrences were found among 1,099 records. This represents approximately 16.47% of the records.

After removal, 918 unique records remained.

Repeated records can cause certain observations to appear more frequently than they should. This can distort the representation of the underlying data and give repeated patterns greater influence.

Removing exact duplicate records therefore improves the structural integrity of the dataset by ensuring that repeated identical observations are not unnecessarily represented multiple times.

---

## Impact on Machine Learning

Duplicate records can affect machine learning models because repeated observations may receive disproportionate influence during training.

For example, if an identical observation occurs multiple times, the model may effectively see that observation as more important than a unique observation that appears only once.

Duplicates can also create a more serious problem when identical records appear in both training and testing datasets. In that situation, the model may encounter the same information during training and evaluation, resulting in data leakage.

Data leakage can produce overly optimistic evaluation results because the test data is no longer completely independent of the training data.

Removing exact duplicate rows before model training helps maintain a cleaner dataset and reduces the risk of duplicated observations influencing model training or evaluation.

---

## Conclusion

The custom duplicate comparison algorithm successfully checked the primary Cleveland Heart Disease dataset and found no exact duplicate rows among its 303 records.

The algorithm was then validated using a separate heart disease dataset containing duplicate records. It detected 181 duplicate rows among 1,099 records and reduced the dataset to 918 unique records.

This demonstrates that the duplicate detection and removal functions operate dynamically on the supplied data rather than relying on hardcoded duplicate counts.

The task also demonstrates why duplicate removal is an important preprocessing step for maintaining data integrity and avoiding potential issues such as disproportionate training influence and data leakage in machine learning workflows.
