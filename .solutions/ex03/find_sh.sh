#!/bin/sh
# Use the script directory as the search root so behavior is local to ex03
DIR="$(cd "$(dirname "$0")" && pwd)"
find "$DIR" -type f -name '*.sh' -print | sed 's|.*/\([^/]*\)\.sh$|\1|' | sort -u