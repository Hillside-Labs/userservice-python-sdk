import grpc
from user_pb2 import *
import user_pb2_grpc


class UserService:
    def __init__(self, addr, creds=None):
        self.addr = addr
        self.creds = creds
        self._stub = None
        self._channel = None

    def __getattr__(self, name):
        if self._channel is None:
            self._channel = grpc.insecure_channel(self.addr)
        if self._stub is None:
            self._stub = user_pb2_grpc.UsersStub(self._channel)

        return getattr(self._stub, name)


def main():
    us = UserService("localhost:9002", None)

    user = us.Get(UserRequest(id=1))
    print(user)


if __name__ == "__main__":
    main()
