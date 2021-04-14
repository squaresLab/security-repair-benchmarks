all: cve_2017_5974 cve_2017_5975 cve_2017_5976

PROGRAM_NAME=zziplib

cve_2017_5974:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3a4ffcd \
	  --build-arg BUG_DIR="$@"

cve_2017_5975:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=33d6e9c \
	  --build-arg BUG_DIR="$@"

cve_2017_5976:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3a4ffcd \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2017_5974 cve_2017_5975 cve_2017_5976
