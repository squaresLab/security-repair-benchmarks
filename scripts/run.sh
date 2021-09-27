#!/bin/bash
HERE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BENCHMARK_IMAGE="secbugs"
VOLUME_HIFIX="hifix_opt"
VOLUME_LLVM="llvm11_opt"
RESULTS_DIR="${HERE_DIR}/../results"
VOLUME_Z3="z3_opt"

mkdir -p "${RESULTS_DIR}"

docker run \
  --volume "${VOLUME_HIFIX}:/opt/hifix" \
  --volume "${VOLUME_LLVM}:/opt/llvm11" \
  --volume "${VOLUME_Z3}:/opt/z3" \
  --env UMASK=0000 \
  -v "${RESULTS_DIR}:/results" \
  --rm \
  -it \
  "${BENCHMARK_IMAGE}"
