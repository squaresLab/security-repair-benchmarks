all: buggy fixed

buggy: gnubug_19784 gnubug_25003 gnubug_25023 gnubug_26545

fixed: gnubug_19784_fixed gnubug_25003_fixed gnubug_25023_fixed gnubug_26545_fixed

PROGRAM_NAME=coreutils

CP_CMD="cp ../../../scripts/sanitizer_parser.py .; cp ../../../scripts/gen_llvm.py .;cp ../../../scripts/getSanitizerInfo_2.sh getSanitizerInfo.sh; cp ../../../scripts/asan_symbolize.py ."

gnubug_19784:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=658529a \
	  --build-arg BUG_DIR="$@"

gnubug_25003:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=68c5eec \
	  --build-arg BUG_DIR="$@"

gnubug_25023:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=ca99c52 \
	  --build-arg BUG_DIR="$@"

gnubug_26545:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=8d34b45 \
	  --build-arg BUG_DIR="$@"

gnubug_19784_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=1d0f1b7 \
	  --build-arg BUG_DIR="gnubug_19784"

gnubug_25003_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=4954f79 \
	  --build-arg BUG_DIR="gnubug_25003"

gnubug_25023_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=d91aee \
	  --build-arg BUG_DIR="gnubug_25023"

gnubug_26545_fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=f4570a9e \
	  --build-arg BUG_DIR="gnubug_26545"

.PHONY: gnubug_19784 gnubug_25003 gnubug_25023 gnubug_26545 gnubug_19784_fixed gnubug_25003_fixed gnubug_25023_fixed gnubug_26545_fixed
