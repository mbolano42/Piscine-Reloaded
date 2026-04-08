#!/bin/sh
# Print MAC addresses, one per line
if [ -d /sys/class/net ]; then
  for d in /sys/class/net/*; do
    addr="$d/address"
    if [ -r "$addr" ]; then
      cat "$addr"
    fi
  done
else
  # Fallback to ip link
  ip link 2>/dev/null | awk '/link\//{print $2}'
fi