#!/bin/sh

gunicorn proxy_server:app -w 4 -k uvicorn.workers.UvicornWorker --reload -b 0.0.0.0:10000 --timeout 0