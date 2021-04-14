all: bugzilla_2611 bugzilla_2633 cve_2016_10092 cve_2016_10094 cve_2016_10272 cve_2016_3186 cve_2016_5314 cve_2016_5321 cve_2016_9273 cve_2016_9532 cve_2017_5225 cve_2017_7595 cve_2017_7599 cve_2017_7600 cve_2017_7601

PROGRAM_NAME=libtiff

bugzilla_2611:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=9a72a69 \
	  --build-arg BUG_DIR="$@"

bugzilla_2633:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=f3069a5 \
	  --build-arg BUG_DIR="$@"

cve_2016_10092:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

cve_2016_10094:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_10272:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

cve_2016_3186:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_5314:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_5321:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_9273:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=6a984bf \
	  --build-arg BUG_DIR="$@"

cve_2016_9532:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=d651abc \
	  --build-arg BUG_DIR="$@"

cve_2017_5225:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=393881d \
	  --build-arg BUG_DIR="$@"

cve_2017_7595:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=2c00d31 \
	  --build-arg BUG_DIR="$@"

cve_2017_7599:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3cfd62d \
	  --build-arg BUG_DIR="$@"

cve_2017_7600:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3cfd62d \
	  --build-arg BUG_DIR="$@"

cve_2017_7601:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3144e57 \
	  --build-arg BUG_DIR="$@"


.PHONY: bugzilla_2611 bugzilla_2633 cve_2016_10092 cve_2016_10094 cve_2016_10272 cve_2016_3186 cve_2016_5314 cve_2016_5321 cve_2016_9273 cve_2016_9532 cve_2017_5225 cve_2017_7595 cve_2017_7599 cve_2017_7600 cve_2017_7601
