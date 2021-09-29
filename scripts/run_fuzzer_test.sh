#!/bin/bash
HERE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BENCHMARK_IMAGE="secbugs"
VOLUME_HIFIX="hifix_opt"
VOLUME_LLVM="llvm11_opt"
VOLUME_FUZZER="${HERE_DIR}/fuzzer_opt"
RESULTS_DIR="${HERE_DIR}/../results"
LOG_DIR="${HERE_DIR}/../logs"
VOLUME_Z3="z3_opt"

mkdir -p "${RESULTS_DIR}"
mkdir -p "${LOG_DIR}"

# docker run \
#   --volume "${VOLUME_HIFIX}:/opt/hifix" \
#   --volume "${VOLUME_LLVM}:/opt/llvm11" \
#   --volume "${VOLUME_Z3}:/opt/z3" \
#   --volume "${VOLUME_FUZZER}:/opt/fuzzer" \
#   --env UMASK=0000 \
#   -v "${RESULTS_DIR}:/results" \
#   -v "${LOG_DIR}:/logs" \
#   --rm \
#   -it \
#   "${BENCHMARK_IMAGE}"

docker run \
  --volume "${VOLUME_FUZZER}:/opt/fuzzer" \
  --env UMASK=0000 \
  -v "${RESULTS_DIR}:/results" \
  -v "${LOG_DIR}:/logs" \
  --rm \
  -it \
  "${BENCHMARK_IMAGE}"
