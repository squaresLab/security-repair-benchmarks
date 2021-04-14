all: cve_2013_7437

PROGRAM_NAME=potrace

cve_2013_7437:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2013_7437
