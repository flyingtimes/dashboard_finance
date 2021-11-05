docker run -it --name pysandbox --rm -v $PWD/sandbox:/usr/src/app -v $PWD/sqlite_data:/usr/src/sqlite_data -v $PWD/data:/usr/src/data pysandbox python3 run.py
