#!/bin/bash

# Description: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

# Package the code
mv project3-chatbot.zip .old.project3-chatbot.zip
zip project3-chatbot.zip -r lambda_function.py main/

# Download dependencies to local directory - Targeted directory
mkdir .package
pip install --target ./.package requests
pip install --target ./.package python-dotenv
pip install --target ./.package alpaca-trade-api
pip install --target ./.package pandas
pip install --target ./.package statsmodels
pip install --target ./.package pandas-datareader

# Add the dependencies to the package root
cd .package
zip -r ../project3-chatbot.zip .
cd ..

# Upload and deploy the function code to AWS Lambda (yes it is "fileb://" not "file://" for some reason..."binary"...)
#aws lambda update-function-code --function-name TailwindTradersBotLambdaFunction --zip-file fileb://project3-chatbot.zip
