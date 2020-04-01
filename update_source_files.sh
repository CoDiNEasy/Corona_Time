#!/usr/bin/env bash

# cd v-env/lib/python3.8/site-packages

# zip -r9 ${OLDPWD}/function.zip .

# cd $OLDPWD

zip -g -j function.zip ./Corona_Time/lambda/us-east-1_ask-custom-Corona_Time-default/lambda_function.py
zip -g -j function.zip ./Corona_Time/lambda/us-east-1_ask-custom-Corona_Time-default/business_logic_json.py

aws lambda update-function-code --function-name ask-custom-Corona_Time-default --zip-file fileb://function.zip
