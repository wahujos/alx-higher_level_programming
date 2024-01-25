#!/bin/bash
# takes url and display all http methods the server will accept
curl -sI "$1" | grep Allow | cut -d' ' -f2-
