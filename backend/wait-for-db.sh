#!/bin/sh

echo "Waiting for MySQL..."

sleep 10

echo "Starting Flask Application..."

exec "$@"
