#!/bin/bash
# a Bash script that sends a custom header variable
curl -s -L -X GET "$1" -H "X-School-User-Id: 98"
