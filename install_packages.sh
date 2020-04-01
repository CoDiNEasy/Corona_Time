#!/usr/bin/env bash

# virtualenv --python=/usr/local/bin/python3.7 v-env

source v-env/bin/activate

pip install ask-sdk
pip install boto3
pip install Pillow
pip install pandas

# yes | pip uninstall numpy

deactivate
