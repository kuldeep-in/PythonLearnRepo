"""
A short demonstration of the Pandas library.
"""

import pandas as pd

print("Example Pandas DataFrame")

exercise_data_raw = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

exercise_df = pd.DataFrame(exercise_data_raw)

print(exercise_df)

print("Selecting rows in a DataFrame")

print(exercise_df.iloc[0:2])

print("Filtering a DataFrame using a value")

filtered_exercise_df = exercise_df.loc[exercise_df["calories"] > 380]
print(filtered_exercise_df)