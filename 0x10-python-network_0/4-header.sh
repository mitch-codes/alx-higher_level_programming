#!/bin/bash
# send header along with request
curl -sH "X-School-User-Id: 98" "$1"
