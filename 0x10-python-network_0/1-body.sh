#!/bin/bash
# Script that displays the body of 200 status code response
curl -sL -w "%{http_code}\\n" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
