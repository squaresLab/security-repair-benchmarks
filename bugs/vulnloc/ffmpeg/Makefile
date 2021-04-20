all: bugchrom_1404 cve_2017_9992

PROGRAM_NAME=ffmpeg

bugchrom_1404:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=0953736b7e \
	  --build-arg BUG_DIR="$@"

cve_2017_9992:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=0953736b7e \
	  --build-arg BUG_DIR="$@"

.PHONY: bugchrom_1404 cve_2017_9992
