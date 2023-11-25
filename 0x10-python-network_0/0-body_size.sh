#!/bin/bash
# Create bash file that gets content length fro http response message
curl -sI "$1" | grep "content-length:" | grep -Eo '[0-9]{1,4}'
