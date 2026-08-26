# Task 03 — Missing Value Identification and Imputation

## 1. Objective

The objective of this task was to identify missing values in the Cleveland Heart Disease dataset without using built-in Pandas functions such as `isna()` or `dropna()`, apply multiple imputation techniques, and justify the most suitable method for the affected columns.

The following imputation techniques were implemented manually:

- Mean imputation
- Median imputation
- Mode imputation

---

## 2. Dataset

The dataset used for this task is the Cleveland Heart Disease dataset.

It contains:

- **303 records**
- **14 columns**

Missing values in the original dataset are represented by the `?` character.

During manual dataset loading, each `?` value was converted to Python `None`.

This allowed missing values to be identified using normal Python conditions instead of relying on Pandas missing-value functions.

---

## 3. Missing Value Identification

The dataset was checked column by column and row by row.

A value was considered missing when:

```python
row[column] is None

No use was made of:

isna()
dropna()
Pandas DataFrame functions for missing-value detection

The following missing values were found:

Column	Missing Values
Ca	4
Thal	2

All remaining columns contained zero missing values.

Therefore, the dataset contained 6 missing values in total.

4. Imputation Techniques

Three different imputation techniques were manually implemented and tested.

4.1 Mean Imputation

Mean imputation replaces a missing value with the arithmetic mean of the available values in the same column.

The formula used was:

Mean = Sum of valid values / Number of valid values

The calculated mean values were:

Column	Mean
Ca	0.6722
Thal	4.7342

Mean imputation successfully replaced all missing values.

However, it was not selected as the final method because the affected columns contain discrete values. A value such as 0.6722 is not a meaningful value for the number of major vessels, and 4.7342 does not represent an actual Thal category.

4.2 Median Imputation

Median imputation replaces a missing value with the middle value of the sorted valid values.

The calculated median values were:

Column	Median
Ca	0
Thal	3

Median imputation successfully replaced all missing values.

For both affected columns, the median produced valid values that already exist within the respective data distributions.

4.3 Mode Imputation

Mode imputation replaces a missing value with the most frequently occurring valid value in the column.

The calculated mode values were:

Column	Mode
Ca	0
Thal	3

Mode imputation also successfully replaced all missing values.

5. Comparison of the Methods

The results obtained from the three techniques were:

Column	Missing	Mean	Median	Mode
Ca	4	0.6722	0	0
Thal	2	4.7342	3	3

All three methods were implemented and tested rather than selecting a method without comparison.

After each method was applied, the affected column was checked again to verify that no missing values remained.

Verification Results
Column	Before	Mean After	Median After	Mode After
Ca	4	0	0	0
Thal	2	0	0	0

This confirms that all three techniques successfully handled the missing values.

6. Selected Method
Mode Imputation

Mode imputation was selected as the final method for this dataset.

The main reason is the nature of the two affected columns.

Ca

The Ca feature represents the number of major vessels. It is a discrete count-like value.

The three calculated replacement values were:

Mean   = 0.6722
Median = 0
Mode   = 0

Using the mean would introduce a fractional value, which does not represent a meaningful number of vessels.

Both median and mode produce 0, which is a valid value in the dataset.

Mode was selected because it uses the most frequently occurring valid value and therefore does not introduce a value that was not observed in the column.

Thal

The Thal feature contains discrete diagnostic categories.

The calculated replacement values were:

Mean   = 4.7342
Median = 3
Mode   = 3

The mean is not suitable because 4.7342 does not represent an actual diagnostic category.

Both median and mode produce 3.

Mode was selected because it directly preserves the most frequently occurring valid category in the original data.

7. Why Mode Was Preferred

The final decision was based on the actual characteristics of the affected columns rather than simply choosing one statistical technique for every situation.

Mode was preferred because:

Both affected features contain discrete values.
Mean imputation can produce fractional values that are not meaningful for these features.
Mode produces actual values already present in the dataset.
Mode and median produced the same replacement values for both affected columns.
Mode directly represents the most frequently observed value in each column.

Therefore, the final replacement values were:

Column	Selected Method	Replacement Value
Ca	Mode	0
Thal	Mode	3
8. Verification After Imputation

The imputation process was verified by counting the remaining missing values after replacement.

The results were:

Ca:
Missing Before = 4
Missing After  = 0

Thal:
Missing Before = 2
Missing After  = 0

Thus, all 6 missing values were successfully handled.

The original dataset file was not modified. A freshly loaded copy of the dataset was used when applying each imputation method.

9. Implementation Constraints

The task specifically required missing-value handling without relying on Pandas built-in functions.

The implementation therefore used:

Manual file parsing
Python lists and dictionaries
None for missing values
Manual mean calculation
Manual median calculation
Manual mode calculation
Manual replacement of missing values

No isna() or dropna() operations were used.

10. Conclusion

This task demonstrated the complete process of identifying and handling missing values manually.

The dataset contained 6 missing values:

4 in Ca
2 in Thal

Mean, median, and mode imputation were implemented and tested.

Although all three methods successfully removed the missing values, mode imputation was selected because the affected features contain discrete values and mode preserves an actual, frequently occurring value from the dataset.

The final selected replacements were:

Ca   → 0
Thal → 3

The implementation successfully reduced the missing-value count for both affected columns from 6 total missing values to 0.