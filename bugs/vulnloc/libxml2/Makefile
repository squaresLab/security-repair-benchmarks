all: buggy fixed

buggy: cve_2012_5134 cve_2016_1838 cve_2016_1839 cve_2017_5969

fixed: cve_2012_5134_fixed cve_2016_1838_fixed cve_2016_1839_fixed cve_2017_5969_fixed

PROGRAM_NAME=libxml2

CP_CMD="cp ../../../scripts/sanitizer_parser.py .; cp ../../../scripts/gen_llvm.py .;cp ../../../scripts/getSanitizerInfo_2.sh getSanitizerInfo.sh; cp ../../../scripts/asan_symbolize.py ."

cve_2012_5134:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=4ea74a44 \
	  --build-arg BUG_DIR="$@"

cve_2016_1838:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=cbb27165 \
	  --build-arg BUG_DIR="$@"

cve_2016_1839:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=db07dd61 \
	  --build-arg BUG_DIR="$@"

cve_2017_5969:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=362b3229 \
	  --build-arg BUG_DIR="$@"

cve_2012_5134_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=6a36fbe3 \
	  --build-arg BUG_DIR="cve_2012_5134"

cve_2016_1838_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=db07dd61 \
	  --build-arg BUG_DIR="cve_2016_1838"

cve_2016_1839_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=a820dbea \
	  --build-arg BUG_DIR="cve_2016_1839"

cve_2017_5969_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=94691dc8 \
	  --build-arg BUG_DIR="cve_2017_5969"

.PHONY: cve_2012_5134 cve_2016_1838 cve_2016_1839 cve_2017_5969 cve_2012_5134_fixed cve_2016_1838_fixed cve_2016_1839_fixed cve_2017_5969_fixed
