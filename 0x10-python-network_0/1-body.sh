#!/bin/bash
# Script that displays the body of 200 status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
