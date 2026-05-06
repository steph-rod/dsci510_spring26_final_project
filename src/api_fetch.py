import requests
import pandas as pd

from config import OPENFDA_URL

def openfda_data(limit=50):
    url = f"{OPENFDA_URL}?limit={limit}"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])
    return pd.DataFrame(results)

if __name__ == "__main__":
    df = openfda_data(50)
    print(df.head())
