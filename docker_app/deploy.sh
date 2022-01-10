#!/bin/bash

V=$(date "+%Y%m%d_%H%M%S")
PROJECT="lunex"
REPO_NAME="app_job"

# build docker
docker build -t $PROJECT/$REPO_NAME .
