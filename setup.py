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
      package_data={
          "mock": [
            "logging.cfg"
          ]
      },
      install_requires=[
          "Faker==5.8.0",
          "sqlalchemy==1.3.22",
          "pandas==1.1.5",
          "pyarrow==3.0.0",
          "xlrd==2.0.1",
          "xlwt==1.3.0",
          "pytest==6.2.2",
          "pytest-cov==2.11.1"],
      zip_safe=False
)
