#!/bin/bash
# Script that displays size of the body of the response
curl -s "$1" | wc -c
