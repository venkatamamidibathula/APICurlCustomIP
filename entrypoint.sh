#!/bin/bash
IP=$1
DNS=$2
CURL_CMD="${@:3}"
if [ -z "$IP" ] || [ -z "$DNS" ] || [ -z "$CURL_CMD" ]; then
  echo "Usage: <IP> <DNS> <curl command>"
  exit 1
fi
echo "$IP $DNS" >> /etc/hosts
eval $CURL_CMD
