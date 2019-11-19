python_grpc:
	source venv/bin/activate &&\
	cd proto_templates &&\
	python -m grpc_tools.protoc rome.proto -I=. --python_out=../lib --grpc_python_out=../lib &&\
	cd ../lib &&\
	cp * ../romulus &&\
	cp * ../remus

run:
	docker-compose build &&\
	docker-compose up