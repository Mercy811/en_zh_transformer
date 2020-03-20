#!/bin/bash

# start_server.sh path/to/OpenNMT-tf
# run this file to start REST server 

# the following line is used to get the path when this script is inside OpenNMT-tf folder
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

DIR=$1
cd $DIR

export IP="0.0.0.0"
export PORT=5000
export URL_ROOT="/translator"
export CONFIG="${DIR}/available_models/flask.conf.json"

python3 server.py --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG
