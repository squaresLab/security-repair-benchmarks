#!/bin/bash
set -eu

SOURCE="${1}"
TARGET="${2}"

pushd project
PROJECT_CFLAGS="-lm"  # TODO could be included in bug.json?
clang "${SOURCE}" "${PROJECT_CFLAGS:-}" "${KLEE_CFLAGS:-}" -o "${TARGET}"
