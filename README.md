# mock ![test](https://github.com/abmamo/mock/workflows/test/badge.svg?branch=main)

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
  # currently supported file types are: "csv", "json", "parquet", "xls"
  # currently supported data types are: "name", "job", "address", "currency", "profile"
  file_generator = FileGenerator(data_size=10, file_type="csv", data_types="name")
  # store data in current dir
  file_generator.store()
  # store data in specific dir
  # file_generator.store(data_dir="<some directory to save data to>")
  # generate files with specific name
  # file_generator.store(file_name="<some file name to save generated file with>)
```
## Logging
By default logging level is set to `WARNING`. To see full logs
```
    import logging
    # change default logging level
    logging.getLogger('mock').setLevel(logging.DEBUG)
    # before importing libs configure logger level
    from mock import *
```
