import requests
import pandas as pd

def openfda_data(limit=50):
    url = f"https://api.fda.gov/drug/enforcement.json?limit={limit}"
    response = requests.get(url)

    data = response.json()
    results = data.get("results", [])

    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    df = openfda_data(50)
    print(df.head())

