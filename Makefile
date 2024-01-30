HATCH = $(shell which hatch)

hatch:
	pip install


protos:
	python -m grpc_tools.protoc -I ../userservice/rpc/userapi --python_out=./src/userservice --pyi_out=./src/userservice --grpc_python_out=./src/userservice ../userservice/rpc/userapi/user.proto
