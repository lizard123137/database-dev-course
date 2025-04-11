# database-dev-course

This repository contains work done during my university database course.

For the project I am using `PostgreSQL` for the `sql` section and `MongoDB` for the `nosql` section.

The project documentation is written in the Polish language, as specified, by the course requirements.

The course materials are publicly available [here](https://dsc.pollub.pl/sql).

### Running the project

Both of the sections have a `Dockerfile` inside of them.

Running the `SQL` module:
``` bash
cd sql
docker build --tag 'database-dev-sql' .
docker run 'database-dev-sql'
```

**Currently the `NoSQL` module `Dockerfile` is not working properly, so you need to install `mongo` locally.**
Running the `NoSQL` module:
``` bash
cd nosql
python3 init.py
```