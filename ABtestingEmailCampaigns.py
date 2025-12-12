# Re-import required libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Rename campaigns to basic names
campaigns_no_dce_renamed = [
    {"name": "Campaign A", "mean": 16, "std_dev": 14.72},
    {"name": "Campaign B", "mean": 11.25, "std_dev": 5.38},
    {"name": "Campaign C", "mean": 59.5, "std_dev": 23.13},
    {"name": "Campaign D", "mean": 19.67, "std_dev": 13.85},
    {"name": "Campaign E", "mean": 17.83, "std_dev": 7.14},
    {"name": "Campaign F", "mean": 35.6, "std_dev": 23.13}
]

# Generate x values for plotting
x = np.linspace(-20, 100, 1000)

# Create the plot with renamed campaigns
plt.figure(figsize=(12, 8))
for campaign in campaigns_no_dce_renamed:
    # Calculate the normal distribution for each campaign
    y = norm.pdf(x, loc=campaign["mean"], scale=campaign["std_dev"])
    plt.plot(x, y, label=campaign["name"])

# Add plot details
plt.title("Bell-Shaped Curves for Email Campaign CTRs (Renamed Campaigns)", fontsize=14)
plt.xlabel("Click-Through Rate (%)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.legend(loc="upper right", fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()
