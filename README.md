# mock ![build](https://github.com/abmamo/mock/workflows/build/badge.svg?branch=main)

package to generate real-world looking data. currently supports generating files & SQLite databases. supported filetypes are JSON, CSV, Parquet, and Excel.

## quickstart

clone repo
```
  git clone https://github.com/abmamo/mock
```
install package
```
  pip3 install /path/to/mock
```
to generate SQLite data
```
  from mock import SQLiteGenerator
  # init sqlite generator
  sqlite_generator = SQLiteGenerator(data_size=10, db_name="mock.db")
  # store data to dir
  sqlite_generator.store(data_dir="<some directory to save data to>")
```
to generate files
```
  from mock import FileGenerator
  # init file generator
  file_generator = FileStorage(data_size=10, file_types=["csv", "json"], data_types=["name", "job", "profile"])
  # store data to dir
  file_generator.store(data_dir="<some directory to save data to>")
```
by default logging level is set to `ERROR` to change this do
```
import logging
from mock import logger as mock_logger
mock_logger.setLevel(logging.INFO)
```
before importing generator classes (SQLiteGenerator and FileGenerator)
