#!/bin/bash
# get list of request methods allowed
curl -sI "$1" | grep "allow" | cut -d " " -f2-
