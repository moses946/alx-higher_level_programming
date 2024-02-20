#!/bin/bash
# Script that displays the body of 200 status code response
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi.
