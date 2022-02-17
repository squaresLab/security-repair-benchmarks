all: bugzilla_2611 bugzilla_2633 cve_2016_10092 cve_2016_10094 cve_2016_10272 cve_2016_3186 cve_2016_5314 cve_2016_5321 cve_2016_9273 cve_2016_9532 cve_2017_5225 cve_2017_7595 cve_2017_7599 cve_2017_7600 cve_2017_7601 cve_2017_7601-multi-pos  cve_2016_10092-multi-pos cve_2017_760x-known-good 
	
fixed: bugzilla_2611-fixed bugzilla_2633-fixed cve_2016_10092-fixed cve_2016_10094-fixed cve_2016_10272-fixed cve_2016_3186-fixed cve_2016_5314-fixed cve_2016_5321-fixed cve_2016_9273-fixed cve_2016_9532-fixed cve_2017_5225-fixed cve_2017_7595-fixed cve_2017_7599-fixed cve_2017_7600-fixed cve_2017_7601-fixed cve_2016_10092-multi-pos-fixed

PROGRAM_NAME=libtiff
CP_CMD="cp ../../../scripts/sanitizer_parser.py .; cp ../../../scripts/gen_llvm.py .;cp ../../../scripts/getSanitizerInfo_2.sh getSanitizerInfo.sh"

bugzilla_2611:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=9a72a69 \
	  --build-arg BUG_DIR="$@"

bugzilla_2633:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=f3069a5 \
	  --build-arg BUG_DIR="$@"

cve_2016_10092:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

cve_2016_10094:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_10272:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

cve_2016_3186:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_5314:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_5321:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

cve_2016_9273:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=6a984bf \
	  --build-arg BUG_DIR="$@"

cve_2016_9532:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=d651abc \
	  --build-arg BUG_DIR="$@"

cve_2017_5225:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=393881d \
	  --build-arg BUG_DIR="$@"

cve_2017_7595:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=2c00d31 \
	  --build-arg BUG_DIR="$@"

cve_2017_7599:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3cfd62d \
	  --build-arg BUG_DIR="$@"

cve_2017_7600:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3cfd62d \
	  --build-arg BUG_DIR="$@"

cve_2017_7601:
	eval ${CP_CMD}
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3144e57 \
	  --build-arg BUG_DIR="$@"

cve_2016_10092-multi-pos:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

cve_2017_7601-multi-pos:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3144e57 \
	  --build-arg BUG_DIR="$@"

# SUT_VERSION=0a76a8c  <= does not fix test for cve_2017_7601
cve_2017_760x-known-good:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=d57ccfc \
	  --build-arg BUG_DIR="$@"


#   FIXED IMAGES
bugzilla_2611-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=43bc256 \
	  --build-arg BUG_DIR="$@"

bugzilla_2633-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=5ed9fea \
	  --build-arg BUG_DIR="$@"

cve_2016_10092-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=9657bbe \
	  --build-arg BUG_DIR="$@"

#  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes 
cve_2016_10094-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=c715336 \
	  --build-arg BUG_DIR="$@"

cve_2016_10272-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=9657bbe \
	  --build-arg BUG_DIR="$@"

# source.zip updated with fix
cve_2016_3186-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes \
	  --build-arg BUG_DIR="$@"

#  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes 
cve_2016_5314-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=391e77f \
	  --build-arg BUG_DIR="$@"

#  --build-arg SUT_GET_CODE_FROM_ARCHIVE=yes 
cve_2016_5321-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=2f79856 \
	  --build-arg BUG_DIR="$@"

cve_2016_9273-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=d651abc \
	  --build-arg BUG_DIR="$@"

cve_2016_9532-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=21d39de \
	  --build-arg BUG_DIR="$@"

cve_2017_5225-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=5c08029 \
	  --build-arg BUG_DIR="$@"

cve_2017_7595-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=47f2fb6 \
	  --build-arg BUG_DIR="$@"

cve_2017_7599-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3144e57 \
	  --build-arg BUG_DIR="$@"

cve_2017_7600-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=3144e57 \
	  --build-arg BUG_DIR="$@"

cve_2017_7601-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
	  --build-arg SUT_VERSION=0a76a8c \
	  --build-arg BUG_DIR="$@"

cve_2016_10092-multi-pos-fixed:
	docker build . -t "${PROGRAM_NAME}-$@" \
          --build-arg SUT_VERSION=9657bbe \
          --build-arg BUG_DIR="$@"

.PHONY: bugzilla_2611 bugzilla_2633 cve_2016_10092 cve_2016_10094 cve_2016_10272 cve_2016_3186 cve_2016_5314 cve_2016_5321 cve_2016_9273 cve_2016_9532 cve_2017_5225 cve_2017_7595 cve_2017_7599 cve_2017_7600 cve_2017_7601 cve_2017_7601-multi-pos cve_2017_760x-known-good bugzilla_2611-fixed bugzilla_2633-fixed cve_2016_10092-fixed cve_2016_10094-fixed cve_2016_10272-fixed cve_2016_3186-fixed cve_2016_5314-fixed cve_2016_5321-fixed cve_2016_9273-fixed cve_2016_9532-fixed cve_2017_5225-fixed cve_2017_7595-fixed cve_2017_7599-fixed cve_2017_7600-fixed cve_2017_7601-fixed cve_2016_10092-multi-pos cve_2016_10092-multi-pos-fixed
