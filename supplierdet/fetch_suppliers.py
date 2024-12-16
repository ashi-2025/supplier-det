import requests

def fetch_suppliers():
    url = "https://services.odata.org/northwind/northwind.svc/Suppliers?$format=json"
    response = requests.get(url)
    if response.status_code == 200:
        suppliers = response.json()["value"]
        for supplier in suppliers:
            print(f"Supplier Name: {supplier['CompanyName']}, Country: {supplier['Country']}")
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    fetch_suppliers()
