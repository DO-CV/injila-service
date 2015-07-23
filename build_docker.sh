#!/bin/bash
PUSH_TAG="$1"

export DOCKER_REGISTRY="davidok8"
export DOCKERCMD="sudo docker"

${DOCKERCMD} build -t injila-service .


if [ -n "$PUSH_TAG" ]; then

  IMAGE_TAG="injila-service:${PUSH_TAG}"

  echo "Pushing to Docker registry at ${DOCKER_REGISTRY} as ${IMAGE_TAG}"
  ${DOCKERCMD} tag -f injila-service:latest ${DOCKER_REGISTRY}/${IMAGE_TAG}
  ${DOCKERCMD} push ${DOCKER_REGISTRY}/${IMAGE_TAG}
fi
