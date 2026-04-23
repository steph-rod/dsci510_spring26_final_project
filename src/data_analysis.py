from api_fetch import *
import pandas as pd
import matplotlib.pyplot as plt

# Crime Dataset
crime_data = pd.read_csv("../data/OpenJustice_crime_data.csv")

print(crime_data.head())
print(crime_data.columns)

crime_table =  crime_data[["Year", "County", "Month", "Violent_sum", "Property_sum"]]

crime_table = crime_table[crime_table["Year"] == 2024]

crime_table["Violent_sum"] = crime_table["Violent_sum"].astype(int)
crime_table["Property_sum"] = crime_table["Property_sum"].astype(int)

crime_table["total_crime"] = crime_table["Violent_sum"] + crime_table["Property_sum"]

crime_by_county = crime_table.groupby("County")["total_crime"].sum().reset_index()

top_counties = crime_by_county.sort_values(by="total_crime", ascending=False)
print(top_counties.head(15))

# Arrest Dataset
arrest_data = pd.read_csv("../data/OpenJustice_arrest_data.csv")

print(arrest_data.head())
print(arrest_data.columns)

arrest_table = arrest_data[["YEAR", "COUNTY", 'F_DRUGOFF']]
print(arrest_table.head())

arrest_table = arrest_table[arrest_table["YEAR"] == 2024]

arrest_table["F_DRUGOFF"] = arrest_table["F_DRUGOFF"].astype(int)

drug_arrest_by_county = arrest_table.groupby("COUNTY")["F_DRUGOFF"].sum().reset_index()
print(drug_arrest_by_county.head())

top_arrests = drug_arrest_by_county.sort_values(by="F_DRUGOFF", ascending=False)
print(top_arrests.head(15))

# Merge

drug_arrest_by_county.rename(columns={"COUNTY": "County"}, inplace=True)
# AI generated: merging datasets on county
merged_tables = pd.merge(crime_by_county, drug_arrest_by_county, on="County")
print(merged_tables.head())

merged_tables.rename(columns={"total_crime": "TotalCrime", "F_DRUGOFF": "DrugArrests"}, inplace=True)

sort_merged_tables = merged_tables.sort_values(by="TotalCrime", ascending=False)
print(sort_merged_tables.head(15))

print(merged_tables["TotalCrime"].corr(merged_tables["DrugArrests"]))

top15_table= sort_merged_tables.head(15)
print(top15_table)
print(len(top15_table))

merged_tables.to_csv("../data/data_hotspots.csv", index=False)
top15_table.to_csv("../data/data_top15_hotspots.csv", index=False)

# api_fetch
fda_data = openfda_data(500)
print(fda_data.head())

fda_data = fda_data[fda_data["state"] == "CA"]
print(fda_data.head())
print(fda_data.columns)

drug_activity = fda_data.groupby("city").size().reset_index(name="DrugReports")
print(drug_activity.sort_values(by="DrugReports", ascending=False).head(15))

#matplotlib
# AI generated: creating visualizations
top15_table.plot(x="County", y=["TotalCrime", "DrugArrests"], kind="bar")

plt.title("Top 15 Counties: Crime vs Drug Arrests in 2024")
plt.xlabel("County")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig("../results/data_top15_hotspots_plot.png")
plt.show()

sort_merged_tables.plot(x="County", y=["TotalCrime", "DrugArrests"],kind="bar")
plt.title("All Counties: Crime vs Drug Arrests in 2024")
plt.xlabel("County")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig("../results/data_hotspots_plot.png")
plt.show()

merged_tables.plot(x="TotalCrime", y="DrugArrests", kind="scatter")
plt.title("Crime vs Drug Arrests in 2024")
plt.xlabel("Total Crime")
plt.ylabel("Drug Arrests")
plt.tight_layout()
plt.savefig("../results/data_hotspots_plot.png")
plt.show()

top_cities = drug_activity.sort_values(by="DrugReports", ascending=False).head(10)

top_cities.plot(x="city", y="DrugReports", kind="bar", legend=False)
plt.title("Top Cities by Drug Reports (openFDA) - 2024")
plt.xlabel("City")
plt.ylabel("Number of Reports")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../results/api_top_cities.png")
plt.show()


