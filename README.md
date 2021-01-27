# mock ![build](https://github.com/abmamo/mock/workflows/build/badge.svg?branch=main)

package to generate real-world looking data. currently supports generating files & SQLite databases. supported filetypes are JSON, CSV, Parquet, and Excel. (needs python 3.7+)

## quickstart
create virtualenv
```
  python3 -m venv env && source env/bin/activate && pip3 install --upgrade pip
```
install mock
```
  pip3 install mock @ https://github.com/abmamo/mock/archive/v0.0.1.tar.gz
```
### SQLite
to generate SQLite data
```
  from mock import SQLiteGenerator
  # init sqlite generator
  sqlite_generator = SQLiteGenerator(data_size=10)
  # store data in current dir
  sqlite_generator.store()
  # store data in a specific dir
  # sqlite_generator.store(data_dir="<some directory to save data to>")
  # store data in a specific sqlite db
  # sqlite_generator.store(db_name="generated.db")
```
### Files
to generate files
```
  from mock import FileGenerator
  # init file generator
  # currently supported file types are: ["csv", "json", "parquet", "xls"]
  # currently supported data types are: ['name', 'job', 'address', 'currency', 'profile']
  file_generator = FileGenerator(data_size=10, file_types=["csv", "json"], data_types=["name", "job", "profile"])
  # store data in current dir
  file_generator.store()
  # store data in specific dir
  # file_generator.store(data_dir="<some directory to save data to>")
  # generate files with specific name
  # file_generator.store(file_name="<some file name to save each file type with>)
```
### Logging
by default logging level is set to `WARNING` to change this do
```
  import logging
  mock.logger.setLevel(logging.INFO)
```
before importing generator classes (SQLiteGenerator and FileGenerator)
