#!/bin/bash
# Script takes URL sends a POST request an displays the body.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"