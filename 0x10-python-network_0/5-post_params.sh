#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
