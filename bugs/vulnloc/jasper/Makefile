all: cve_2016_8691 cve_2016_9557

PROGRAM_NAME=jasper

cve_2016_8691:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg BUG_DIR="$@"

cve_2016_9557:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2016_8691 cve_2016_9557
