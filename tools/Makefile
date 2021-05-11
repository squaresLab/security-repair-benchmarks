all: extractfix hifix

extractfix:
	docker build -t extractfix ExtractFix

hifix:
	make -C HiFix/docker

.PHONY: extractfix hifix
