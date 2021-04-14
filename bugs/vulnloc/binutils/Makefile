all: binutils-cve_2017_14745 binutils-cve_2017_15020 binutils-cve_2017_15025 binutils-cve_2017_6965

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

.PHONY: binutils-cve_2017_14745 binutils-cve_2017_15020 binutils-cve_2017_15025 binutils-cve_2017_6965
