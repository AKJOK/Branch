import requests

def fetch_swagger_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching Swagger JSON:", e)
        return None

def extract_endpoints(swagger_json):
    endpoints = []
    paths = swagger_json.get("paths", {})
    for path in paths:
        endpoints.append(path)
    return endpoints

def main():
    swagger_url = input("Enter the URL of the Swagger JSON: ")
    
    swagger_json = fetch_swagger_json(swagger_url)
    if swagger_json:
        endpoints = extract_endpoints(swagger_json)
        print("Endpoints present in Swagger:")
        for endpoint in endpoints:
            print(endpoint)
    else:
        print("Failed to fetch Swagger JSON. Check the URL and try again.")

if __name__ == "__main__":
    main()

