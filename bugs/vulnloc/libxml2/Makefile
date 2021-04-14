all: cve_2012_5134 cve_2016_1838 cve_2016_1839 cve_2017_5969

PROGRAM_NAME=libxml2

cve_2012_5134:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=4ea74a44 \
	  --build-arg BUG_DIR="$@"

cve_2016_1838:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=cbb27165 \
	  --build-arg BUG_DIR="$@"

cve_2016_1839:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=db07dd61 \
	  --build-arg BUG_DIR="$@"

cve_2017_5969:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=362b3229 \
	  --build-arg BUG_DIR="$@"

.PHONY: cve_2012_5134 cve_2016_1838 cve_2016_1839 cve_2017_5969
