
# Device connection parameters
device_params = {
    "host": "example-device",
    "port": 830,
    "username": "admin",
    "password": "password",
    "hostkey_verify": False,
}

# YANG XML payload for interface configuration
xml_payload = """
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:example:module">
        <interface>
            <name>GigabitEthernet0/0</name>
            <!-- Other configuration parameters -->
        </interface>
    </interfaces>
</config>
"""

# NETCONF operation to configure the interface
with manager.connect(**device_params) as m:
    # Edit-config operation to apply configuration changes
    m.edit_config(target="running", config=xml_payload)
