#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sI $1 | tail -n4 | head -n1 | cut -d " " -f2 | cut -c1-2
