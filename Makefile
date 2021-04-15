all: benchmark

bugs:
	make -C bugs

tools:
	make -C tools

benchmark: bugs tools
	docker build -t secbugs .

.PHONY: bugs tools benchmark
