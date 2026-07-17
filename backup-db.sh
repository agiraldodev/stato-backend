#!/bin/bash

set -a
source .env
set +a

docker exec -t stato-postgres \
pg_dump -U $POSTGRES_USER -d $POSTGRES_DB \
> backup.sql