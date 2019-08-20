#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI $1 | tail -n4 | head -n1 | cut -d " " -f2-
