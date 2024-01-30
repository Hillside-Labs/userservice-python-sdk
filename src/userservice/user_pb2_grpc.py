# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/userapi.Users/Create',
                request_serializer=user__pb2.NewUser.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/userapi.Users/Get',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/userapi.Users/Update',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.Find = channel.unary_unary(
                '/userapi.Users/Find',
                request_serializer=user__pb2.UserQuery.SerializeToString,
                response_deserializer=user__pb2.UserListResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/userapi.Users/Delete',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.LogEvent = channel.unary_unary(
                '/userapi.Users/LogEvent',
                request_serializer=user__pb2.EventRequest.SerializeToString,
                response_deserializer=user__pb2.EventResponse.FromString,
                )
        self.SearchUserTraits = channel.unary_unary(
                '/userapi.Users/SearchUserTraits',
                request_serializer=user__pb2.SearchUserTraitsRequest.SerializeToString,
                response_deserializer=user__pb2.SearchUserTraitsResponse.FromString,
                )
        self.GetUsersByTraits = channel.unary_unary(
                '/userapi.Users/GetUsersByTraits',
                request_serializer=user__pb2.SearchUserTraitsRequest.SerializeToString,
                response_deserializer=user__pb2.UserListResponse.FromString,
                )
        self.GetUsersByAggregatedTraits = channel.unary_unary(
                '/userapi.Users/GetUsersByAggregatedTraits',
                request_serializer=user__pb2.GetUsersByAggregatedTraitsRequest.SerializeToString,
                response_deserializer=user__pb2.UserListResponse.FromString,
                )
        self.GetAggregateForUsers = channel.unary_unary(
                '/userapi.Users/GetAggregateForUsers',
                request_serializer=user__pb2.GetAggregateForUsersRequest.SerializeToString,
                response_deserializer=user__pb2.AggregateResponse.FromString,
                )
        self.GetUsersByEvents = channel.unary_unary(
                '/userapi.Users/GetUsersByEvents',
                request_serializer=user__pb2.SearchUserEventsRequest.SerializeToString,
                response_deserializer=user__pb2.UserListResponse.FromString,
                )
        self.SearchEvents = channel.unary_unary(
                '/userapi.Users/SearchEvents',
                request_serializer=user__pb2.SearchEventsRequest.SerializeToString,
                response_deserializer=user__pb2.SearchEventsResponse.FromString,
                )
        self.NaturalBreaks = channel.unary_unary(
                '/userapi.Users/NaturalBreaks',
                request_serializer=user__pb2.NaturalBreaksRequest.SerializeToString,
                response_deserializer=user__pb2.NaturalBreaksResponse.FromString,
                )
        self.NaturalBreaksQueried = channel.unary_unary(
                '/userapi.Users/NaturalBreaksQueried',
                request_serializer=user__pb2.NaturalBreaksQueryRequest.SerializeToString,
                response_deserializer=user__pb2.NaturalBreaksResponse.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchUserTraits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersByTraits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersByAggregatedTraits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAggregateForUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersByEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NaturalBreaks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NaturalBreaksQueried(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=user__pb2.NewUser.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=user__pb2.UserQuery.FromString,
                    response_serializer=user__pb2.UserListResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'LogEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.LogEvent,
                    request_deserializer=user__pb2.EventRequest.FromString,
                    response_serializer=user__pb2.EventResponse.SerializeToString,
            ),
            'SearchUserTraits': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchUserTraits,
                    request_deserializer=user__pb2.SearchUserTraitsRequest.FromString,
                    response_serializer=user__pb2.SearchUserTraitsResponse.SerializeToString,
            ),
            'GetUsersByTraits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersByTraits,
                    request_deserializer=user__pb2.SearchUserTraitsRequest.FromString,
                    response_serializer=user__pb2.UserListResponse.SerializeToString,
            ),
            'GetUsersByAggregatedTraits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersByAggregatedTraits,
                    request_deserializer=user__pb2.GetUsersByAggregatedTraitsRequest.FromString,
                    response_serializer=user__pb2.UserListResponse.SerializeToString,
            ),
            'GetAggregateForUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAggregateForUsers,
                    request_deserializer=user__pb2.GetAggregateForUsersRequest.FromString,
                    response_serializer=user__pb2.AggregateResponse.SerializeToString,
            ),
            'GetUsersByEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersByEvents,
                    request_deserializer=user__pb2.SearchUserEventsRequest.FromString,
                    response_serializer=user__pb2.UserListResponse.SerializeToString,
            ),
            'SearchEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchEvents,
                    request_deserializer=user__pb2.SearchEventsRequest.FromString,
                    response_serializer=user__pb2.SearchEventsResponse.SerializeToString,
            ),
            'NaturalBreaks': grpc.unary_unary_rpc_method_handler(
                    servicer.NaturalBreaks,
                    request_deserializer=user__pb2.NaturalBreaksRequest.FromString,
                    response_serializer=user__pb2.NaturalBreaksResponse.SerializeToString,
            ),
            'NaturalBreaksQueried': grpc.unary_unary_rpc_method_handler(
                    servicer.NaturalBreaksQueried,
                    request_deserializer=user__pb2.NaturalBreaksQueryRequest.FromString,
                    response_serializer=user__pb2.NaturalBreaksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'userapi.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/Create',
            user__pb2.NewUser.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/Get',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/Update',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/Find',
            user__pb2.UserQuery.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/Delete',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/LogEvent',
            user__pb2.EventRequest.SerializeToString,
            user__pb2.EventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchUserTraits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/SearchUserTraits',
            user__pb2.SearchUserTraitsRequest.SerializeToString,
            user__pb2.SearchUserTraitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersByTraits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/GetUsersByTraits',
            user__pb2.SearchUserTraitsRequest.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersByAggregatedTraits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/GetUsersByAggregatedTraits',
            user__pb2.GetUsersByAggregatedTraitsRequest.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAggregateForUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/GetAggregateForUsers',
            user__pb2.GetAggregateForUsersRequest.SerializeToString,
            user__pb2.AggregateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersByEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/GetUsersByEvents',
            user__pb2.SearchUserEventsRequest.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/SearchEvents',
            user__pb2.SearchEventsRequest.SerializeToString,
            user__pb2.SearchEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NaturalBreaks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/NaturalBreaks',
            user__pb2.NaturalBreaksRequest.SerializeToString,
            user__pb2.NaturalBreaksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NaturalBreaksQueried(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userapi.Users/NaturalBreaksQueried',
            user__pb2.NaturalBreaksQueryRequest.SerializeToString,
            user__pb2.NaturalBreaksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
