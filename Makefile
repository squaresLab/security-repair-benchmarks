all: benchmark

init:
	git submodule update --init --recursive tools/Darjeeling tools/Kaskara

bugs: init
	make -C bugs

tools: init
	make -C tools

benchmark: bugs
	docker build -f docker/Dockerfile.benchmark -t secbugs .

.PHONY: bugs init tools benchmark
