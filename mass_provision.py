import grpc
import csv
import api.device_pb2 as device_pb2
import api.device_pb2_grpc as device_pb2_grpc
import api.application_pb2 as application_pb2
import api.application_pb2_grpc as application_pb2_grpc
import api.common_pb2 as common_pb2

# Define the ChirpStack server address
CHIRPSTACK_SERVER = "127.0.0.1:8080"

# Function to read API key from file
def get_api_key(file_path="test-key1.txt"):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()  # Read the key and remove spaces/newlines
    except FileNotFoundError:
        print("Error: API key file not found. Please create 'test-key1.txt' and add the API key.")
        exit(1)

# Load API key from file
API_KEY = get_api_key()

# Create a gRPC channel and client stubs
channel = grpc.insecure_channel(CHIRPSTACK_SERVER)
device_client = device_pb2_grpc.DeviceServiceStub(channel)
application_client = application_pb2_grpc.ApplicationServiceStub(channel)

# Function to get application ID dynamically
def get_application_id(application_name):
    metadata = [("authorization", f"Bearer {API_KEY}")]
    request = application_pb2.ListApplicationsRequest(limit=10, offset=0, tenant_id="<YOUR-TENANT-ID>")
    
    response = application_client.List(request, metadata=metadata)
    
    for app in response.result:
        if app.name == application_name:
            return app.id
    
    print(f"Error: Application '{application_name}' not found.")
    exit(1)

# Set your ChirpStack Application Name (Modify as per your setup)
APPLICATION_NAME = "LoRa-button-app"
APPLICATION_ID = get_application_id(APPLICATION_NAME)

# Function to register a device
def create_device(dev_eui, name, description, app_key):
    metadata = [("authorization", f"Bearer {API_KEY}")]
    
    # Step 1: Create device request
    device_request = device_pb2.CreateDeviceRequest(
        device=device_pb2.Device(
            dev_eui=dev_eui,
            name=name,
            description=description,
            application_id=APPLICATION_ID,
            device_profile_id="<YOUR-DEVICE-PROFILE-ID>"
        )
    )

    # Step 2: Send gRPC request to create the device
    try:
        device_client.Create(device_request, metadata=metadata)
        print(f"Device {name} ({dev_eui}) registered successfully!")
    except grpc.RpcError as e:
        print(f"Error creating device {name}: {e.details()}")

    # Step 3: Create device keys request (for OTAA)
    if app_key:
        keys_request = device_pb2.CreateDeviceKeysRequest(
            device_keys=device_pb2.DeviceKeys(
                dev_eui=dev_eui,
                nwk_key=app_key,
                app_key=app_key
            )
        )

        # Step 4: Send gRPC request to create device keys
        try:
            device_client.CreateKeys(keys_request, metadata=metadata)
            print(f"AppKey added for {name} ({dev_eui})")
        except grpc.RpcError as e:
            print(f"Error adding keys for {name}: {e.details()}")

# Function to read devices from CSV and register them
def register_devices_from_csv(file_path="devices.csv"):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            dev_eui = row["dev_eui"].strip()
            name = row["name"].strip()
            description = row["description"].strip()
            app_key = row["app_key"].strip()
            
            create_device(dev_eui, name, description, app_key)

# Run the mass provisioning script
register_devices_from_csv()
