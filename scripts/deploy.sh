#!/bin/bash

# curl -dH -X POST $azurewebhook        Module 11
curl -dH -X POST "$(terraform output -raw webhook_url)"     # Module 12
