bootstrap:
	hatch env create

protos:
  mkdir protos
  cp ../userservice-proto/user.proto ./protos/

	python -m grpc_tools.protoc \
		--proto_path ../userservice-proto/ \
		--python_out=./src/userservice \
		--pyi_out=./src/userservice \
		--grpc_python_out=./src/userservice \
		../userservice-proto/user.proto
