all: gnubug_19784 gnubug_25003 gnubug_25023 gnubug_26545

PROGRAM_NAME=coreutils

gnubug_19784:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=658529a \
	  --build-arg BUG_DIR="$@"

gnubug_25003:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=68c5eec \
	  --build-arg BUG_DIR="$@"

gnubug_25023:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=ca99c52 \
	  --build-arg BUG_DIR="$@"

gnubug_26545:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=8d34b45 \
	  --build-arg BUG_DIR="$@"

.PHONY: gnubug_19784 gnubug_25003 gnubug_25023 gnubug_26545
