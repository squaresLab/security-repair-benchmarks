all: buggy fixed

buggy: binutils-cve_2017_14745 binutils-cve_2017_15020 binutils-cve_2017_15025 binutils-cve_2017_6965

fixed: binutils-cve_2017_14745_fixed binutils-cve_2017_15020_fixed binutils-cve_2017_15025_fixed binutils-cve_2017_6965_fixed

binutils-cve_2017_14745:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=7a31b38ef87d133d8204cae67a97f1989d25fa18 \
	  --build-arg BUG_DIR=cve_2017_14745

binutils-cve_2017_15020:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=11855d8a1f11b102a702ab76e95b22082cccf2f8 \
	  --build-arg BUG_DIR=cve_2017_15020

binutils-cve_2017_15025:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=515f23e63c0074ab531bc954f84ca40c6281a724 \
	  --build-arg BUG_DIR=cve_2017_15025

binutils-cve_2017_6965:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=53f7e8ea7fad1fcff1b58f4cbd74e192e0bcbc1d \
	  --build-arg BUG_DIR=cve_2017_6965

binutils-cve_2017_14745_fixed:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=e6ff33ca50c1180725dde11c84ee93fcdb4235ef \
	  --build-arg BUG_DIR=cve_2017_14745

binutils-cve_2017_15020_fixed:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=1da5c9a485f3dcac4c45e96ef4b7dae5948314b5 \
	  --build-arg BUG_DIR=cve_2017_15020

binutils-cve_2017_15025_fixed:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=d8010d3e75ec7194a4703774090b27486b742d48 \
	  --build-arg BUG_DIR=cve_2017_15025

binutils-cve_2017_6965_fixed:
	docker build . -t "$@" \
	  --build-arg SUT_VERSION=03f7786e2f440b9892b1c34a58fb26222ce1b493 \
	  --build-arg BUG_DIR=cve_2017_6965

.PHONY: binutils-cve_2017_14745 binutils-cve_2017_15020 binutils-cve_2017_15025 binutils-cve_2017_6965 binutils-cve_2017_14745_fixed binutils-cve_2017_15020_fixed binutils-cve_2017_15025_fixed binutils-cve_2017_6965_fixed

