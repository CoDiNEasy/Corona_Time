#!/usr/bin/env bash

rm -f ./function.zip
sleep 7

cd v-env/lib/python3.7/site-packages

zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD

zip -g -j function.zip ./Corona_Time/lambda/us-east-1_ask-custom-Corona_Time-default/lambda_function.py
zip -g -j function.zip ./Corona_Time/lambda/us-east-1_ask-custom-Corona_Time-default/business_logic_json.py

aws lambda update-function-code --function-name ask-custom-Corona_Time-default --zip-file fileb://function.zip
