#!/bin/sh
DOCKER_REPO="home_automation_framework"
DOCKER_ACC="dankersw"
IMG_TAG="0.0.2-x86"

echo "Authenticating to Docker hub"
docker login --username=$DOCKER_ACC

echo "Building docker image"
docker build -t $DOCKER_ACC/$DOCKER_REPO:$IMG_TAG .. --build-arg tag=$IMG_TAG

echo "Tagging for local registry and pushing image/tags"
docker push $DOCKER_ACC/$DOCKER_REPO:$IMG_TAG

echo "Cleanup"
docker rmi $DOCKER_ACC/$DOCKER_REPO:$IMG_TAG
