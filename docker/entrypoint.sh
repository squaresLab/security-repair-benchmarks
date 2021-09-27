#!/bin/bash
if [[ ! -z "UMASK" ]]; then
  umask "${UMASK}"
fi

exec "$@"
