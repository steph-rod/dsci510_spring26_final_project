from api_fetch import openfda_data

def test_api():
    df = openfda_data(10)
    assert not df.empty
    print("Test worked")

if __name__ == "__main__":
    test_api()