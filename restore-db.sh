#!/bin/bash

set -a
source .env
set +a

docker exec -i stato-postgres \
psql -U $POSTGRES_USER -d $POSTGRES_DB \
< backup.sql