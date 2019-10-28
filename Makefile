
build: echo-server.py Dockerfile
	docker build . -t echo:1

start:
	docker run -d -p 65432:65432 --rm --name=echo_server echo:1

stop:
	docker stop echo_server

clean:
	rm -r -f var/log/server.log

