import IPFClient
import os

# Set the IPfabric API key
api_key = "<api-key>"

# Initialize the IPFclient object
ipf = IPFClient.IPFClient(api_key=api_key)

# Set the path to the folder where you want to save the device configurations
folder_path = "<path-to-folder>"

# Create the folder if it does not already exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Set the error message to display if an error occurs
error_msg = "An error occurred while retrieving the device configurations: "

try:
    # Get the list of devices from IPfabric
    devices = ipf.devices.list()

    # Iterate through the devices and download their configurations
    for device in devices:
        # Get the configuration for the device
        config = ipf.devices.get_config(device_id=device["id"])
        # Set the name of the file
        filename = f"{device['name']}.txt"
        # Set the full path to the file
        file_path = os.path.join(folder_path, filename)
        # Write the device configuration to the file
        with open(file_path, "w") as f:
            f.write(config)
except IPFClient.exceptions.IPFClientError as e:
    # If an error occurs, print the error message
    print(error_msg, e)