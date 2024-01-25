#!/bin/bash
# ends a JSON POST request to a URL passed as the first argument,
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
