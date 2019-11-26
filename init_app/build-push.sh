#!/bin/bash
echo "Enter Tag > "
if read TAG; then
    echo "tag entered $TAG"
    NO_CACHE=$(date +%s)
    docker build . -t wsmathias9/secretmng:$TAG --no-cache --build-arg NO_CACHE=$NO_CACHE \
    && docker push wsmathias9/secretmng:$TAG
fi
