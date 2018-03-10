#!/bin/bash

set -x

mkdir -p ~/.aws
touch ~/.aws/credentials

echo "
[default]
region = us-west-2
aws_access_key_id=$AWS_ACCESS_KEY_ID
aws_secret_access_key=$AWS_SECRET_ACCESS_KEY
[vgs-dev]
region = us-west-2
role_arn = arn:aws:iam::883127560329:role/VGSStageDeploy
source_profile = default
" | tee -a ~/.aws/credentials
