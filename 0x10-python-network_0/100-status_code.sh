#!/bin/bash
# Sends a request to a Url passed and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
