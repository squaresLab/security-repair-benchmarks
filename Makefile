all: benchmark

init:
	git submodule update --init --recursive

bugs: init
	make -C bugs

tools: init
	make -C tools

benchmark: bugs tools
	docker build -t secbugs .

.PHONY: bugs init tools benchmark
