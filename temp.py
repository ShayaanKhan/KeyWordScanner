import pandas as pd

# Define the input CSV file path and output CSV file path
input_csv_file = "top10milliondomains.csv"
output_csv_file = "top10milliondomains.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Define a list of valid website extensions
valid_extensions = [".com", ".net", ".co", ".to", ".io",]  # Add more extensions if needed

# Filter the DataFrame to keep only rows with valid extensions
filtered_df = df[df["Domain"].str.lower().str.endswith(tuple(valid_extensions))]

# Save the filtered DataFrame to a CSV file
filtered_df.to_csv(output_csv_file, index=False)

print(
    f"Rows with valid extensions {', '.join(valid_extensions)} kept and saved to {output_csv_file}"
)
