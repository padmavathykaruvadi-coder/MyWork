# covid_eda.py
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, csv_path="country_wise_latest.csv", output_dir="outputs"):
        self.csv_path = csv_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.df_raw = None
        self.df = None           # selected features
        self.cleaned_df = None   # outliers removed
        self.scaled_df = None    # normalized

    # 1) Load + keep only required columns
    def load_and_select(self):
        self.df_raw = pd.read_csv(self.csv_path)

        # Handle possible naming variants safely
        cols_map = {c.lower().strip(): c for c in self.df_raw.columns}
        needed_lower = ["confirmed", "new cases"]
        missing = [c for c in needed_lower if c not in cols_map]
        if missing:
            raise ValueError(
                f"Required columns missing: {missing}. "
                f"Found columns: {list(self.df_raw.columns)}"
            )

        confirmed_col = cols_map["confirmed"]
        newcases_col = cols_map["new cases"]
        self.df = self.df_raw[[confirmed_col, newcases_col]].copy()
        self.df.columns = ["Confirmed", "New cases"]  # normalize names

    # 2) Statistical measures
    def compute_statistics(self):
        print("\n--- Statistical Measures (raw) ---")
        mean_vals = self.df.mean(numeric_only=True)
        median_vals = self.df.median(numeric_only=True)
        var_vals = self.df.var(numeric_only=True, ddof=1)
        std_vals = self.df.std(numeric_only=True, ddof=1)
        corr_matrix = self.df.corr(numeric_only=True)

        print("Mean:\n", mean_vals)
        print("\nMedian:\n", median_vals)
        print("\nVariance:\n", var_vals)
        print("\nStandard Deviation:\n", std_vals)
        print("\nCorrelation Matrix:\n", corr_matrix)

        return {
            "mean": mean_vals,
            "median": median_vals,
            "variance": var_vals,
            "std": std_vals,
            "corr": corr_matrix,
        }

    # 3) Outlier detection & removal (IQR)
    def remove_outliers_iqr(self):
        q1 = self.df.quantile(0.25)
        q3 = self.df.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        mask = ~(((self.df < lower) | (self.df > upper)).any(axis=1))
        self.cleaned_df = self.df[mask].reset_index(drop=True)

        removed = len(self.df) - len(self.cleaned_df)
        print(f"\n--- IQR Outlier Removal ---\nRemoved rows: {removed}")
        print("\nCleaned data (first 10 rows):")
        print(self.cleaned_df.head(10))

        # Save cleaned
        cleaned_path = os.path.join(self.output_dir, "cleaned_covid.csv")
        self.cleaned_df.to_csv(cleaned_path, index=False)
        print(f"\nSaved cleaned dataset → {cleaned_path}")

    # 4) Normalization (StandardScaler) on cleaned data
    def normalize_standard(self):
        scaler = StandardScaler()
        scaled = scaler.fit_transform(self.cleaned_df[["Confirmed", "New cases"]])
        self.scaled_df = pd.DataFrame(scaled, columns=["Confirmed_scaled", "NewCases_scaled"])
        scaled_path = os.path.join(self.output_dir, "scaled_covid.csv")
        self.scaled_df.to_csv(scaled_path, index=False)
        print(f"\nSaved scaled dataset → {scaled_path}")
        print("\nScaled data (first 10 rows):")
        print(self.scaled_df.head(10))

    # 5a) Histograms (before & after normalization)
    def plot_histograms(self):
        sns.set(style="whitegrid")

        # BEFORE normalization
        for col in ["Confirmed", "New cases"]:
            plt.figure()
            sns.histplot(self.df[col].dropna(), kde=True, bins=30)
            plt.title(f"Histogram (Before Normalization): {col}")
            plt.xlabel(col)
            out_path = os.path.join(self.output_dir, f"hist_before_{col.replace(' ','_').lower()}.png")
            plt.tight_layout()
            plt.savefig(out_path, dpi=150)
            plt.close()
            print(f"Saved → {out_path}")

        # AFTER normalization
        for col in ["Confirmed_scaled", "NewCases_scaled"]:
            plt.figure()
            sns.histplot(self.scaled_df[col].dropna(), kde=True, bins=30)
            plt.title(f"Histogram (After Normalization): {col}")
            plt.xlabel(col)
            out_path = os.path.join(self.output_dir, f"hist_after_{col.lower()}.png")
            plt.tight_layout()
            plt.savefig(out_path, dpi=150)
            plt.close()
            print(f"Saved → {out_path}")

    # 5b) Heatmap (correlation)
    def plot_heatmap(self):
        corr = self.cleaned_df[["Confirmed", "New cases"]].corr()
        plt.figure()
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
        plt.title("Correlation Heatmap (Cleaned Data)")
        out_path = os.path.join(self.output_dir, "heatmap_correlation.png")
        plt.tight_layout()
        plt.savefig(out_path, dpi=150)
        plt.close()
        print(f"Saved → {out_path}")

    # Convenience runner
    def run(self):
        self.load_and_select()
        self.compute_statistics()
        self.remove_outliers_iqr()
        self.normalize_standard()
        self.plot_histograms()
        self.plot_heatmap()
        print("\n✅ EDA completed.")

if __name__ == "__main__":
    # Change path if your CSV is elsewhere
    eda = CovidEDA(csv_path="country_wise_latest.csv")
    eda.run()
