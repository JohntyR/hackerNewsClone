#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
NEW_TRAVIS_REPO_SLUG=$(echo "$TRAVIS_REPO_SLUG" | tr '[:upper:]' '[:lower:]')
NEW_TAG=$(echo "$TAG" | tr '[:upper:]' '[:lower:]')
docker build -f Dockerfile -t $NEW_TRAVIS_REPO_SLUG:$NEW_TAG .
docker push $NEW_TRAVIS_REPO_SLUG:$NEW_TAG