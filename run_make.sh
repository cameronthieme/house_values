#!/bin/bash

# Install dependencies
make requirements

# download raw data
make getdata

# clean data
make cleandata

# Train XGBoost model
make train

# predict output on test data
make predict
