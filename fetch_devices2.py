import grpc
import api.device_pb2 as device_pb2
import api.device_pb2_grpc as device_pb2_grpc
import api.application_pb2 as application_pb2
import api.application_pb2_grpc as application_pb2_grpc

# Define the ChirpStack server address
CHIRPSTACK_SERVER = "127.0.0.1:8080"


# Function to read API key from a file
def get_api_key(file_path="test-key1.txt"):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()  # Read the key and remove any extra spaces/newlines
    except FileNotFoundError:
        print("Error: API key file not found. Please create 'api_key.txt' and add the API key.")
        exit(1)

# Load API key from file
API_KEY = get_api_key()

# Create a gRPC channel to connect to ChirpStack
channel = grpc.insecure_channel(CHIRPSTACK_SERVER)

# Create gRPC client stubs
app_client = application_pb2_grpc.ApplicationServiceStub(channel)
device_client = device_pb2_grpc.DeviceServiceStub(channel)

# Prepare the gRPC metadata (Authorization token)
metadata = [("authorization", f"Bearer {API_KEY}")]

# Step 1: Fetch Application ID
app_request = application_pb2.ListApplicationsRequest(limit=1, offset=0, tenant_id="52f14cd4-c6f1-4fbd-8f87-4025e1d49242")
app_response = app_client.List(app_request, metadata=metadata)

if app_response.result:
    application_id = app_response.result[0].id  # Get the first application ID
    print(f"Fetched Application ID: {application_id}")

    # Step 2: Fetch Devices using the retrieved Application ID
    device_request = device_pb2.ListDevicesRequest(limit=10, offset=0, application_id=application_id)
    device_response = device_client.List(device_request, metadata=metadata)

    # Print the device response
    print("Devices List:", device_response)
else:
    print("No applications found!")
