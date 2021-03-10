#!/bin/bash

# Description: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

# Package the code
mv project3-chatbot.zip .old.project3-chatbot.zip
zip project3-chatbot.zip -r lambda_function.py main/

# Download dependencies to local directory - Targeted directory
pip install --target ./.package requests
pip install --target ./.package python-dotenv
pip install --target ./.package alpaca-trade-api
pip install --target ./.package pandas
pip install --target ./.package statsmodels

# Add the dependencies to the package root
mkdir .package
cd .package
zip -r ../project3-chatbot.zip .
cd ..

# Upload and deploy the function code to AWS Lambda
#aws lambda update-function-code --function-name project2_get_recommended_portfolio --zip-file fileb://litquidity-chatbot.zip

