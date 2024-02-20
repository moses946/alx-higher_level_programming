#!/bin/bash
# Bash script that makes a request to a URL
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
