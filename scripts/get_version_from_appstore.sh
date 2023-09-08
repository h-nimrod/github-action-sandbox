#!/bin/bash

base_url="https://itunes.apple.com/lookup"
bundle_id=$1
country=$2

if [ -z "$bundle_id" ]; then
  echo "Usage: bash get_version_from_appstore.sh <app_id> [country_code]"
  exit 1
fi

response=$(curl -s -G -d "bundleId=$bundle_id" -d "country=$country" "$base_url")

result_count=$(echo $response | jq '.resultCount')

if [ $result_count -eq 0 ]; then
  echo "not found"
  exit 1
fi

version=$(echo $response | jq -r '.results[0].version')
echo -n $version
