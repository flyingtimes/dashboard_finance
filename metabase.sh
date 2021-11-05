docker run -it --rm -v $PWD/sqlite_data/:/data --name metabase -e MB_DB_FILE=/data/metabase.db -e MUID=$UID -e MGID=$GID -p 3000:3000 metabase/metabase
