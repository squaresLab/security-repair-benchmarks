all: extractfix hifix fuzzer

extractfix:
	docker build -t extractfix ExtractFix

hifix:
	make -C HiFix/docker

fuzzer:
	docker build -t fuzzer VulnLoc

.PHONY: extractfix hifix fuzzer
