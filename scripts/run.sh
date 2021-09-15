#!/bin/bash
BENCHMARK_IMAGE="secbugs"
VOLUME_HIFIX="hifix_opt"
VOLUME_LLVM="llvm11_opt"
VOLUME_Z3="z3_opt"

docker run \
  --volume "${VOLUME_HIFIX}:/opt/hifix" \
  --volume "${VOLUME_LLVM}:/opt/llvm11" \
  --volume "${VOLUME_Z3}:/opt/z3" \
  --rm \
  -it \
  "${BENCHMARK_IMAGE}"
