#!/usr/bin/env bash

# virtualenv --python=/usr/local/bin/python3.7 v-env

source v-env/bin/activate

pip install ask-sdk
pip install boto3
pip install Pillow
pip install json
pip install requests
pip install datetime
pip install timedelta

deactivate
