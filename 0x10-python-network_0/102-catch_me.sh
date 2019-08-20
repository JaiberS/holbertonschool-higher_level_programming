#!/bin/bash
# catch the catch me file
curl -d "user_id=98" -H "Origin: HolbertonSchool" -LX PUT 0.0.0.0:5000/catch_me
