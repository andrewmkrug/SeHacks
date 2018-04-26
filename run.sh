#!/usr/bin/env bash

docker run -it -v $PWD:/repo -p 9000:9000 store/gitpitch/desktop:personal