#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sI 0.0.0.0:5000 | tail -n4 | head -n1 | cut -d " " -f2 
