all: cve_2016_9264 cve_2018_8806 cve_2018_8964

PROGRAM_NAME=libming

cve_2016_9264:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=cc6a386 \
	  --build-arg BUG_DIR="$@"

cve_2018_8806:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=c4d20b1 \
	  --build-arg BUG_DIR="$@"

cve_2018_8964:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=c4d20b1 \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2016_9264 cve_2018_8806 cve_2018_8964
