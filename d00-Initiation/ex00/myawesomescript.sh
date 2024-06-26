#!/bin/sh

#  url test: bit.ly/1O72s3U

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <bit.ly URL>"
  exit 1
fi

bitly_url=$1

response=$(curl -s -I "$bitly_url")

real_url=$(echo "$response" | grep -i "Location:" | cut -d ' ' -f2)

echo "$real_url"
