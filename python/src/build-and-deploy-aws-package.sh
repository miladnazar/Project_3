#!/bin/bash

# Description: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

# Package the code
mv litquidity-chatbot.zip .old.litquidity-chatbot.zip
zip litquidity-chatbot.zip -r lambda_function.py main/

# Download dependencies to local directory - Targeted directory
pip install --target ./.package requests
pip install --target ./.package python-dotenv
pip install --target ./.package alpaca-trade-api
pip install --target ./.package pandas
pip install --target ./.package statsmodels

# Add the dependencies to the package root
cd .package
zip -r ../litquidity-chatbot.zip .
cd ..

# Upload and deploy the function code to AWS Lambda
#aws lambda update-function-code --function-name project2_get_recommended_portfolio --zip-file fileb://litquidity-chatbot.zip

