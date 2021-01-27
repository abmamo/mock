from setuptools import setup, find_packages


# read the contents of README file
from os import path
# get current file directory
this_directory = path.abspath(path.dirname(__file__))
# open README with UTF-8 encoding
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    # read README
    long_description = f.read()

setup(
      name='mock',
      version='0.0.1',
      description='generate fake data',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/abmamo/mock',
      author='Abenezer Mamo',
      author_email='contact@abmamo.com',
      license='MIT',
      packages=find_packages(exclude=("tests", "env")),
      install_requires=[
          "Faker==4.14.2",
          "sqlalchemy==1.3.20",
          "pandas==1.1.4",
          "pyarrow==2.0.0",
          "xlrd==2.0.1",
          "xlwt==1.3.0",
          "openpyxl==3.0.5",
          "pytest==6.2.1",
          "pytest-cov==2.10.1"],
      zip_safe=False
)
