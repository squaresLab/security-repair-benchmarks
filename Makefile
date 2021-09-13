all: benchmark

init:
	git submodule update --init --recursive

bugs: init
	make -C bugs

tools: init
	make -C tools

hifix-only: init
	docker build -t secbugs -f Dockerfile.hifix .

benchmark: bugs tools
	docker build -t secbugs .

.PHONY: bugs init tools benchmark
