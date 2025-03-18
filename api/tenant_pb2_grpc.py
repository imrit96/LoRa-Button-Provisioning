# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from api import tenant_pb2 as api_dot_tenant__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in api/tenant_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TenantServiceStub(object):
    """TenantService is the service providing API methods for managing tenants.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/api.TenantService/Create',
                request_serializer=api_dot_tenant__pb2.CreateTenantRequest.SerializeToString,
                response_deserializer=api_dot_tenant__pb2.CreateTenantResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/api.TenantService/Get',
                request_serializer=api_dot_tenant__pb2.GetTenantRequest.SerializeToString,
                response_deserializer=api_dot_tenant__pb2.GetTenantResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/api.TenantService/Update',
                request_serializer=api_dot_tenant__pb2.UpdateTenantRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/api.TenantService/Delete',
                request_serializer=api_dot_tenant__pb2.DeleteTenantRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/api.TenantService/List',
                request_serializer=api_dot_tenant__pb2.ListTenantsRequest.SerializeToString,
                response_deserializer=api_dot_tenant__pb2.ListTenantsResponse.FromString,
                _registered_method=True)
        self.AddUser = channel.unary_unary(
                '/api.TenantService/AddUser',
                request_serializer=api_dot_tenant__pb2.AddTenantUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetUser = channel.unary_unary(
                '/api.TenantService/GetUser',
                request_serializer=api_dot_tenant__pb2.GetTenantUserRequest.SerializeToString,
                response_deserializer=api_dot_tenant__pb2.GetTenantUserResponse.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/api.TenantService/UpdateUser',
                request_serializer=api_dot_tenant__pb2.UpdateTenantUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/api.TenantService/DeleteUser',
                request_serializer=api_dot_tenant__pb2.DeleteTenantUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.ListUsers = channel.unary_unary(
                '/api.TenantService/ListUsers',
                request_serializer=api_dot_tenant__pb2.ListTenantUsersRequest.SerializeToString,
                response_deserializer=api_dot_tenant__pb2.ListTenantUsersResponse.FromString,
                _registered_method=True)


class TenantServiceServicer(object):
    """TenantService is the service providing API methods for managing tenants.
    """

    def Create(self, request, context):
        """Create a new tenant.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get the tenant for the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update the given tenant.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete the tenant with the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Get the list of tenants.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Add an user to the tenant.
        Note: the user must already exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Get the the tenant user for the given tenant and user IDs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Update the given tenant user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Delete the given tenant user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """Get the list of tenant users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TenantServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=api_dot_tenant__pb2.CreateTenantRequest.FromString,
                    response_serializer=api_dot_tenant__pb2.CreateTenantResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=api_dot_tenant__pb2.GetTenantRequest.FromString,
                    response_serializer=api_dot_tenant__pb2.GetTenantResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=api_dot_tenant__pb2.UpdateTenantRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=api_dot_tenant__pb2.DeleteTenantRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=api_dot_tenant__pb2.ListTenantsRequest.FromString,
                    response_serializer=api_dot_tenant__pb2.ListTenantsResponse.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=api_dot_tenant__pb2.AddTenantUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=api_dot_tenant__pb2.GetTenantUserRequest.FromString,
                    response_serializer=api_dot_tenant__pb2.GetTenantUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=api_dot_tenant__pb2.UpdateTenantUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=api_dot_tenant__pb2.DeleteTenantUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=api_dot_tenant__pb2.ListTenantUsersRequest.FromString,
                    response_serializer=api_dot_tenant__pb2.ListTenantUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.TenantService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('api.TenantService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TenantService(object):
    """TenantService is the service providing API methods for managing tenants.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/Create',
            api_dot_tenant__pb2.CreateTenantRequest.SerializeToString,
            api_dot_tenant__pb2.CreateTenantResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/Get',
            api_dot_tenant__pb2.GetTenantRequest.SerializeToString,
            api_dot_tenant__pb2.GetTenantResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/Update',
            api_dot_tenant__pb2.UpdateTenantRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/Delete',
            api_dot_tenant__pb2.DeleteTenantRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/List',
            api_dot_tenant__pb2.ListTenantsRequest.SerializeToString,
            api_dot_tenant__pb2.ListTenantsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/AddUser',
            api_dot_tenant__pb2.AddTenantUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/GetUser',
            api_dot_tenant__pb2.GetTenantUserRequest.SerializeToString,
            api_dot_tenant__pb2.GetTenantUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/UpdateUser',
            api_dot_tenant__pb2.UpdateTenantUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/DeleteUser',
            api_dot_tenant__pb2.DeleteTenantUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.TenantService/ListUsers',
            api_dot_tenant__pb2.ListTenantUsersRequest.SerializeToString,
            api_dot_tenant__pb2.ListTenantUsersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
