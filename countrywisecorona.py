import pandas as pd
import numpy as np

class CovidDataset:
    def __init__(self, csv_path="country_wise_latest.csv"):
        self.df = pd.read_csv(csv_path)
        self.country_col = "Country/Region"
        self.region_col = "WHO Region"

class CovidAnalyzer(CovidDataset):
    def summarize_by_region(self):
        return self.df.groupby(self.region_col)[["Confirmed", "Deaths", "Recovered"]].sum()

    def filter_low_cases(self, min_confirmed=10):
        self.df = self.df[self.df["Confirmed"] >= min_confirmed]
        return self.df

    def highest_confirmed_region(self):
        g = self.df.groupby(self.region_col)["Confirmed"].sum()
        return g.idxmax(), int(g.max())

    def sort_by_confirmed_to_csv(self, out_path="sorted_by_confirmed.csv"):
        s = self.df.sort_values("Confirmed", ascending=False)
        s.to_csv(out_path, index=False)
        return out_path

    def top5_countries(self):
        return self.df[[self.country_col, "Confirmed"]].sort_values("Confirmed", ascending=False).head(5)

    def lowest_death_region(self):
        g = self.df.groupby(self.region_col)["Deaths"].sum()
        return g.idxmin(), int(g.min())

    def india_summary(self):
        sub = self.df[self.df[self.country_col] == "India"]
        if sub.empty:
            return None
        r = sub.iloc[0]
        return {"Confirmed": int(r["Confirmed"]), "Deaths": int(r["Deaths"]), "Recovered": int(r["Recovered"])}

    def mortality_rate_by_region(self):
        g = self.df.groupby(self.region_col).agg({"Deaths":"sum","Confirmed":"sum"})
        g["MortalityRate"] = g["Deaths"]/g["Confirmed"]
        return g[["MortalityRate"]].sort_values("MortalityRate", ascending=False)

    def recovery_rate_by_region(self):
        g = self.df.groupby(self.region_col).agg({"Recovered":"sum","Confirmed":"sum"})
        g["RecoveryRate"] = g["Recovered"]/g["Confirmed"]
        return g[["RecoveryRate"]].sort_values("RecoveryRate", ascending=False)

    def detect_outliers_confirmed(self):
        s = self.df["Confirmed"]
        m, sd = s.mean(), s.std()
        lo, hi = m - 2*sd, m + 2*sd
        o = self.df[(s < lo) | (s > hi)][[self.country_col, "Confirmed"]]
        return o, m, sd, lo, hi

    def group_by_country_region(self):
        return self.df.groupby([self.region_col, self.country_col])[["Confirmed","Deaths","Recovered"]].sum()

    def regions_with_zero_recovered(self):
        g = self.df.groupby(self.region_col)["Recovered"].sum()
        return g[g == 0].index.tolist()

if __name__ == "__main__":
    a = CovidAnalyzer("/Users/MB-921007/Downloads/Project1/country_wise_latest.csv")


    print("\n1) Region Totals:\n", a.summarize_by_region())
    print("\n2) Filtered (Confirmed >=10):\n", a.filter_low_cases().shape)
    print("\n3) Highest Confirmed Region:\n", a.highest_confirmed_region())
    print("\n4) Sorted CSV Path:\n", a.sort_by_confirmed_to_csv())
    print("\n5) Top 5 Countries:\n", a.top5_countries())
    print("\n6) Lowest Death Region:\n", a.lowest_death_region())
    print("\n7) India Summary:\n", a.india_summary())
    print("\n8) Mortality Rate by Region:\n", a.mortality_rate_by_region())
    print("\n9) Recovery Rate by Region:\n", a.recovery_rate_by_region())
    print("\n10) Outliers:\n", a.detect_outliers_confirmed())
    print("\n11) Group by Country & Region:\n", a.group_by_country_region().head(10))
    print("\n12) Regions with Zero Recovered:\n", a.regions_with_zero_recovered())
