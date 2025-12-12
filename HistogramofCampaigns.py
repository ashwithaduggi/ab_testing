import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the Excel sheet (replace 'example.xlsx' with your file path)
file_path = 'Example of Email Data CTR.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Group data by 'Email Campaign' and calculate the mean Click Through Rate (CTR)
grouped_data = df.groupby('Email Campaign').agg(
    Mean_CTR=('Click Through Rate', 'mean'),
    Std_Deviation=('Click Through Rate', 'std')
).reset_index()

# Plotting
plt.figure(figsize=(12, 6))

# Bar graph for Mean CTRs
plt.bar(grouped_data['Email Campaign'], grouped_data['Mean_CTR'], 
        yerr=grouped_data['Std_Deviation'], capsize=5, color="skyblue")

# Labeling
plt.title("Mean Click Through Rate (CTR) by Email Campaign", fontsize=16)
plt.xlabel("Email Campaigns", fontsize=12)
plt.ylabel("Mean Click Through Rate (%)", fontsize=12)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()
