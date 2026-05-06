from api_fetch import openfda_data
from config import STATE, OPENFDA_LIMIT, TOP_CITIES_PLOT
import pandas as pd
import matplotlib.pyplot as plt

# NOTE: Original crime and arrest analysis has been removed
# Raw data files are not included in the repository per guidelines

def main():
    print("Running pipeline without raw datasets (final submission)")

    fda_data = openfda_data(OPENFDA_LIMIT)
    print(fda_data.head())

    fda_data = fda_data[fda_data["state"] == STATE]
    print(fda_data.head())
    print(fda_data.columns)

    drug_activity = fda_data.groupby("city").size().reset_index(name="DrugReports")
    print(drug_activity.sort_values(by="DrugReports", ascending=False).head(15))

    top_cities = drug_activity.sort_values(by="DrugReports", ascending=False).head(10)

    top_cities.plot(x="city", y="DrugReports", kind="bar", legend=False)
    plt.title("Top Cities by Drug Reports (openFDA) - 2024")
    plt.xlabel("City")
    plt.ylabel("Number of Reports")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(TOP_CITIES_PLOT)
    plt.show()

if __name__ == "__main__":
    main()









