import pandas as pd
from ydata_profiling import ProfileReport

# Example dataset
df = pd.read_csv("train.csv")

# Generate EDA report
profile = ProfileReport(df, title="EDA Report", explorative=True)

# Save to HTML
profile.to_file("eda_report.html")
print("Report saved to eda_report.html")
