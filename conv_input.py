import pandas as pd

def replace_values_in_column(csv_file_path, column_name, strings_to_replace):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Check if column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    
    # Replace the values in the column
    df[column_name] = df[column_name].apply(lambda x: strings_to_replace[0] if x in strings_to_replace else x)
    
    # Save the modified DataFrame back to the CSV file (or you can save it to a new file if you prefer)
    df.to_csv(csv_file_path, index=False)
    
    print(f"Values in column '{column_name}' have been replaced.")
    return df

def remove_rows_for_category(df, column_name, category, num_rows_to_remove):
    """
    Removes a specified number of rows for a given category in the specified column.
    """
    # Check if column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
    
    # Filter the rows where the value matches the category
    category_rows = df[df[column_name] == category]
    
    # Check if there are enough rows to remove
    if len(category_rows) < num_rows_to_remove:
        raise ValueError(f"Not enough rows in category '{category}' to remove {num_rows_to_remove} rows.")
    
    # Get the indexes of the rows to remove (first num_rows_to_remove rows)
    rows_to_remove = category_rows.index[:num_rows_to_remove]
    
    # Drop the rows from the DataFrame
    df = df.drop(rows_to_remove)
    
    print(f"Removed {num_rows_to_remove} rows for category '{category}'.")
    return df

# Example usage
csv_file_path = 'input/demo_parcels_25jun2024_grouped_grouped.csv'
column_name = 'ua_grp_id'
strings_to_replace = ['']  # Replace these with your list

df = replace_values_in_column(csv_file_path, column_name, strings_to_replace)

df = remove_rows_for_category(df, 'ua_grp_id', 'EPEZH', 20000)
df = remove_rows_for_category(df, 'ua_grp_id', '7V1D1', 12000)
df = remove_rows_for_category(df, 'ua_grp_id', '9SIS78', 100)
df = remove_rows_for_category(df, 'ua_grp_id', 'RTS5', 100)

df.to_csv(csv_file_path.split('.')[0] + '_grouped.csv', index=False)  # Save to a new file if needed
