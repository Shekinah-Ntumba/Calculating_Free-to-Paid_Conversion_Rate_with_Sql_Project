import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load your data
url = "https://raw.githubusercontent.com/Shekinah-Ntumba/Calculating_Free-to-Paid_Conversion_Rate_with_Sql_Project/refs/heads/main/student_journey_data.csv"
df = pd.read_csv(url)

# Display basic info
print("=== DATA OVERVIEW ===")
print(f"Total students: {len(df)}")
print("\nFirst 5 rows:")
print(df.head())

print("\n=== BASIC STATISTICS ===")
print(df[['days_diff_reg_watch', 'days_diff_watch_purch']].describe())

# Calculate mean vs median to detect outliers
print("\n=== MEAN vs MEDIAN ANALYSIS ===")
for col in ['days_diff_reg_watch', 'days_diff_watch_purch']:
    mean_val = df[col].mean()
    median_val = df[col].median()
    print(f"\n{col}:")
    print(f"  Mean: {mean_val:.2f} days")
    print(f"  Median: {median_val:.2f} days")
    print(f"  Difference: {mean_val - median_val:.2f} days")
    
    if abs(mean_val - median_val) > 5:
        print("  ⚠️  Significant difference suggests outliers!")
    else:
        print("  ✅ Mean and median are close - fewer outliers")

# Find modes (most common values)
print("\n=== MODE ANALYSIS (Most Common Behaviors) ===")
for col in ['days_diff_reg_watch', 'days_diff_watch_purch']:
    mode_vals = df[col].mode()
    print(f"\n{col} modes: {mode_vals.values}")
    if 0 in mode_vals.values or 1 in mode_vals.values:
        print(f"  🎯 Students commonly engage/purchase immediately!")
    
    # Show frequency of top values
    top_values = df[col].value_counts().head(5)
    print(f"  Top 5 values and frequencies:")
    for value, count in top_values.items():
        print(f"    {value} days: {count} students ({count/len(df)*100:.1f}%)")

# Visualize distributions
print("\n=== CREATING VISUALIZATIONS ===")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Distribution plots
sns.histplot(df['days_diff_reg_watch'], bins=50, ax=axes[0,0])
axes[0,0].set_title('Distribution: Registration to First Watch')
axes[0,0].axvline(df['days_diff_reg_watch'].mean(), color='red', linestyle='--', label=f'Mean: {df["days_diff_reg_watch"].mean():.1f}')
axes[0,0].axvline(df['days_diff_reg_watch'].median(), color='green', linestyle='--', label=f'Median: {df["days_diff_reg_watch"].median():.1f}')
axes[0,0].legend()

sns.histplot(df['days_diff_watch_purch'], bins=50, ax=axes[0,1])
axes[0,1].set_title('Distribution: First Watch to Purchase')
axes[0,1].axvline(df['days_diff_watch_purch'].mean(), color='red', linestyle='--', label=f'Mean: {df["days_diff_watch_purch"].mean():.1f}')
axes[0,1].axvline(df['days_diff_watch_purch'].median(), color='green', linestyle='--', label=f'Median: {df["days_diff_watch_purch"].median():.1f}')
axes[0,1].legend()

# Box plots to identify outliers
sns.boxplot(y=df['days_diff_reg_watch'], ax=axes[1,0])
axes[1,0].set_title('Box Plot: Registration to Watch')

sns.boxplot(y=df['days_diff_watch_purch'], ax=axes[1,1])
axes[1,1].set_title('Box Plot: Watch to Purchase')

plt.tight_layout()
plt.show()

# Outlier detection
print("\n=== OUTLIER ANALYSIS ===")
for col in ['days_diff_reg_watch', 'days_diff_watch_purch']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\n{col}:")
    print(f"  Outliers: {len(outliers)} students ({len(outliers)/len(df)*100:.1f}%)")
    print(f"  Outlier range: < {lower_bound:.1f} days or > {upper_bound:.1f} days")
    
    if len(outliers) > 0:
        print(f"  Extreme values: {outliers[col].max()} days (max)")

# Analyze quick converters vs slow deciders
print("\n=== BEHAVIOR SEGMENTATION ===")
quick_engagers = df[df['days_diff_reg_watch'] <= 1]
slow_engagers = df[df['days_diff_reg_watch'] > 7]

quick_converters = df[df['days_diff_watch_purch'] <= 7]
slow_converters = df[df['days_diff_watch_purch'] > 30]

print(f"Quick engagers (≤1 day): {len(quick_engagers)} students ({len(quick_engagers)/len(df)*100:.1f}%)")
print(f"Slow engagers (>7 days): {len(slow_engagers)} students ({len(slow_engagers)/len(df)*100:.1f}%)")
print(f"Quick converters (≤7 days): {len(quick_converters)} students ({len(quick_converters)/len(df)*100:.1f}%)")
print(f"Slow converters (>30 days): {len(slow_converters)} students ({len(slow_converters)/len(df)*100:.1f}%)")
