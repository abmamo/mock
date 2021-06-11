from setuptools import setup, find_packages


# read the contents of README file
from os import path

# get current file directory
this_directory = path.abspath(path.dirname(__file__))
# open README with UTF-8 encoding
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    # read README
    long_description = f.read()

setup(
    name="mock",
    version="0.0.1",
    description="generate fake data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/abmamo/mock",
    author="Abenezer Mamo",
    author_email="contact@abmamo.com",
    license="MIT",
    packages=find_packages(exclude=("tests", "env")),
    install_requires=[
        # generation
        "Faker==5.8.0",
        # db orm (sqlite)
        "sqlalchemy==1.4.18",
        # data man.
        "pandas==1.1.5",
        # parquet
        "pyarrow==3.0.0",
        # excel
        "xlrd==2.0.1",
        "xlwt==1.3.0",
    ],
    zip_safe=False,
)
