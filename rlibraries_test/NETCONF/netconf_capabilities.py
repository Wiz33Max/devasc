from ncclient import manager

# Device connection parameters
device_params = {
    "host": "your_device_ip",
    "port": 830,
    "username": "your_username",
    "password": "your_password",
    "hostkey_verify": False,  # For self-signed certificates
}

# Function to retrieve capabilities from the device
def get_device_capabilities(device_params):
    # Connect to the device
    with manager.connect(**device_params) as m:
        print("Connected to device.")

        # Retrieve capabilities from the device
        capabilities = m.server_capabilities

        # Print the capabilities
        print("\nDevice Capabilities:")
        for cap in capabilities:
            print(cap)

# Call the function to get capabilities
get_device_capabilities(device_params)
