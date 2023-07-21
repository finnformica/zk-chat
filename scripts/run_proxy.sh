#!/bin/sh

gunicorn proxy_server:app -w 4 -k uvicorn.workers.UvicornWorker --reload