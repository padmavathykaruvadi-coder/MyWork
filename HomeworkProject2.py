import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CovidDataset:
    def __init__(self, csv_path="country_wise_latest.csv"):
        self.df = pd.read_csv(csv_path)
        self.country_col = "Country/Region"
        self.region_col = "WHO Region"

class CovidAnalyzer(CovidDataset):
    def summarize_by_region(self):
        return self.df.groupby(self.region_col)[["Confirmed","Deaths","Recovered"]].sum()

class CovidVisualization(CovidAnalyzer):
    def bar_top10_countries_confirmed(self):
        top10 = self.df.nlargest(10,"Confirmed")
        plt.bar(top10[self.country_col],top10["Confirmed"],color="skyblue")
        plt.title("Top 10 Countries by Confirmed Cases")
        plt.xticks(rotation=45,ha="right")
        plt.ylabel("Confirmed Cases")
        plt.show()

    def pie_global_deaths_by_region(self):
        deaths = self.df.groupby(self.region_col)["Deaths"].sum()
        plt.pie(deaths,labels=deaths.index,autopct="%1.1f%%",startangle=140)
        plt.title("Global Death Distribution by Region")
        plt.show()

    def line_confirmed_vs_deaths_top5(self):
        top5 = self.df.nlargest(5,"Confirmed")
        for col in ["Confirmed","Deaths"]:
            plt.plot(top5[self.country_col],top5[col],marker="o",label=col)
        plt.title("Confirmed vs Deaths (Top 5 Countries)")
        plt.legend()
        plt.show()

    def scatter_confirmed_vs_recovered(self):
        plt.scatter(self.df["Confirmed"],self.df["Recovered"],alpha=0.5,color="green")
        plt.title("Confirmed vs Recovered Cases")
        plt.xlabel("Confirmed")
        plt.ylabel("Recovered")
        plt.show()

    def hist_deaths(self):
        plt.hist(self.df["Deaths"],bins=20,color="orange",edgecolor="black")
        plt.title("Histogram of Death Counts")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.show()

    def stacked_bar_top5(self):
        top5 = self.df.nlargest(5,"Confirmed")[[self.country_col,"Confirmed","Deaths","Recovered"]]
        top5.set_index(self.country_col).plot(kind="bar",stacked=True)
        plt.title("Stacked Bar: Confirmed, Deaths, Recovered (Top 5 Countries)")
        plt.ylabel("Counts")
        plt.show()

    def boxplot_confirmed_by_region(self):
        data = [grp["Confirmed"].values for _,grp in self.df.groupby(self.region_col)]
        plt.boxplot(data,labels=self.df[self.region_col].unique())
        plt.title("Boxplot of Confirmed Cases by Region")
        plt.xticks(rotation=45,ha="right")
        plt.ylabel("Confirmed Cases")
        plt.show()

    def trendline_india_vs_country(self,other_country="US"):
        sub = self.df[self.df[self.country_col].isin(["India",other_country])]
        plt.bar(sub[self.country_col],sub["Confirmed"],color=["blue","red"])
        plt.title(f"Confirmed Cases: India vs {other_country}")
        plt.ylabel("Confirmed Cases")
        plt.show()

if __name__ == "__main__":
    viz = CovidVisualization("country_wise_latest.csv")
    viz.bar_top10_countries_confirmed()
    viz.pie_global_deaths_by_region()
    viz.line_confirmed_vs_deaths_top5()
    viz.scatter_confirmed_vs_recovered()
    viz.hist_deaths()
    viz.stacked_bar_top5()
    viz.boxplot_confirmed_by_region()
    viz.trendline_india_vs_country("Brazil")
