#!/bin/bash
# size of the file in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
