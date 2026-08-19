# Network Device Classification Program

devices = {
    "Switch": {
        "layer": "Layer 2 - Data Link Layer",
        "function": "Connects devices in a LAN and forwards frames using MAC addresses."
    },

    "Router": {
        "layer": "Layer 3 - Network Layer",
        "function": "Connects different networks and forwards packets using IP addresses."
    },

    "Bridge": {
        "layer": "Layer 2 - Data Link Layer",
        "function": "Connects two LAN segments and filters network traffic using MAC addresses."
    },

    "Access Point": {
        "layer": "Layer 2 - Data Link Layer",
        "function": "Provides wireless network access to computers, phones and other devices."
    }
}

media = {
    "Twisted Pair": {
        "type": "Guided / Wired",
        "function": "Transmits data using electrical signals through copper wires."
    },

    "Fiber Optic": {
        "type": "Guided / Wired",
        "function": "Transmits data using light signals through optical fibers."
    },

    "Coaxial Cable": {
        "type": "Guided / Wired",
        "function": "Transmits data using electrical signals through a coaxial cable."
    },

    "Wi-Fi / Radio": {
        "type": "Unguided / Wireless",
        "function": "Transmits data through radio waves without physical cables."
    }
}


print("=" * 75)
print("              NETWORK DEVICE CLASSIFICATION REPORT")
print("=" * 75)

for device, details in devices.items():
    print("\nDevice:", device)
    print("Layer of Operation:", details["layer"])
    print("Primary Function:", details["function"])
    print("-" * 75)


print("\n")
print("=" * 75)
print("              TRANSMISSION MEDIA CLASSIFICATION")
print("=" * 75)

for medium, details in media.items():
    print("\nTransmission Medium:", medium)
    print("Type:", details["type"])
    print("Primary Function:", details["function"])
    print("-" * 75)

print("\nClassification completed successfully.")
print("\nClassification completed successfully.")
