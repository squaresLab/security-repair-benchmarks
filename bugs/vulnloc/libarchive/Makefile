all: cve_2016_5844

PROGRAM_NAME=libarchive

cve_2016_5844:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2016_5844
