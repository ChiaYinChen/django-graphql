#!/bin/sh
uvicorn core.asgi:application --host 0.0.0.0 --port 8000 $@