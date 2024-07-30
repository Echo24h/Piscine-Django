#!/bin/bash

# Create a virtual environment named django_venv
python3 -m venv django_venv

# Activate the virtual environment
source django_venv/bin/activate

# Install the requirements
pip install -r requirement.txt