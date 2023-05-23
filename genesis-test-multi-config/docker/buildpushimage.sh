#!/usr/bin/env bash
set -e

Registry="gcr.io/unity-genesis-prd-prd/genesis"
Date=$(date +%Y%m%d)
CommitHash=$(git rev-parse --short HEAD)

cd ../

echo -e ""
echo -e "Build Image\n"
sudo docker build -t $Registry/test-frontend:master-$Date-$CommitHash .
sudo docker build -t $Registry/test-frontend:master .

echo -e ""
echo -e "Push Image\n"
sudo docker push $Registry/test-frontend:master-$Date-$CommitHash
sudo docker push $Registry/test-frontend:master

echo -e ""
echo -e "Pushed: $Registry/test-frontend:master-$Date-$CommitHash"
echo -e "Pushed: $Registry/test-frontend:master"
echo -e ""