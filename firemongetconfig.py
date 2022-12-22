import requests

# Set the base URL for the Firemon API
base_url = "https://<firemon-server>/api/1.0"

# Set the API endpoint for retrieving firewall configurations
endpoint = "/configurations"

# Set the API key for authenticating with the Firemon API
api_key = "<api-key>"

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {api_key}",
}

# Send the API request to retrieve the firewall configurations
response = requests.get(base_url + endpoint, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, the firewall configurations will be in the response data
    firewall_configurations = response.json()
    # You can then iterate through the firewall configurations and save them to a file or do whatever else you need to do with them
    for firewall_config in firewall_configurations:
        print(firewall_config)
else:
    # If the request was not successful, there may be an error in the request or the API may be down
    print("An error occurred while retrieving the firewall configurations:", response.text)