all: cve_2012_2806 cve_2017_15232 cve_2018_14498 cve_2018_19664

PROGRAM_NAME=libjpeg

cve_2012_2806:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_USES_CMAKE=no \
	  --build-arg SUT_VERSION=4f24016 \
	  --build-arg BUG_DIR="$@"

cve_2017_15232:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_USES_CMAKE=no \
	  --build-arg SUT_VERSION=3212005 \
	  --build-arg BUG_DIR="$@"

cve_2018_14498:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_USES_CMAKE=yes \
	  --build-arg SUT_VERSION=0fa7850 \
	  --build-arg BUG_DIR="$@"

cve_2018_19664:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_USES_CMAKE=yes \
	  --build-arg SUT_VERSION=beefb62 \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2012_2806 cve_2017_15232 cve_2018_14498 cve_2018_19664
