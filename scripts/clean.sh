#!/usr/bin/bash

if [ -d '../dist' ] ; then
    rm -r ../dist
fi
if [ -d '../build' ] ; then
    rm -r ../build
fi
if [ -d '../twitter_api_client.egg-info' ] ; then
    rm -r ../twitter_api_client.egg-info
fi