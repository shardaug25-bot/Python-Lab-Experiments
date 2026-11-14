# Experiment 24: Data Cleaning using Pandas

import pandas as pd

# Take CSV filename
filename = input("Enter CSV filename: ")

try:
    # Read dataset
    df = pd.read_csv(filename)

    print("\nOriginal Dataset:")
    print(df)

    # Display missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing numerical values using mean
    for column in df.select_dtypes(include="number").columns:
        df[column] = df[column].fillna(df[column].mean())

    # Handle missing text values using mode
    for column in df.select_dtypes(include="object").columns:
        mode_value = df[column].mode()

        if not mode_value.empty:
            df[column] = df[column].fillna(mode_value[0])
        else:
            df[column] = df[column].fillna("Unknown")

    # Display cleaned dataset
    print("\nCleaned Dataset:")
    print(df)

    # Save cleaned dataset
    df.to_csv("cleaned_data.csv", index=False)

    print("\nCleaned dataset saved as cleaned_data.csv")

except FileNotFoundError:
    print("CSV file not found.")

except pd.errors.EmptyDataError:
    print("CSV file is empty.")

except Exception as e:
    print("Error:", e)