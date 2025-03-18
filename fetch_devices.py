import grpc
import api.device_pb2 as device_pb2
import api.device_pb2_grpc as device_pb2_grpc

# Define the ChirpStack server address
CHIRPSTACK_SERVER = "127.0.0.1:8080"

# API Key (Replace with your actual API key)
API_KEY = "YOUR-API-KEY"

# Create a gRPC channel to connect to ChirpStack
channel = grpc.insecure_channel(CHIRPSTACK_SERVER)

# Create a gRPC client stub
client = device_pb2_grpc.DeviceServiceStub(channel)

# Prepare the gRPC metadata (Authorization token)
metadata = [("authorization", f"Bearer {API_KEY}")]

# Send a request to list devices
request = device_pb2.ListDevicesRequest(limit=10, offset=0, application_id="90839dbc-baec-4752-a3a4-e27df2ff8403")
response = client.List(request, metadata=metadata)

# Print the response
print(response)
