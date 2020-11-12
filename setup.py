from setuptools import setup, find_packages


# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='mock',
      version='0.0.3',
      description='generate fake data',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/abmamo/mock',
      author='Abenezer Mamo',
      author_email='contact@abmamo.com',
      license='MIT',
      packages=find_packages(exclude=("tests", "env")),
      install_requires=["pandas==1.1.2", "sqlalchemy==1.3.20", "pyarrow==0.16.0", "Faker==4.14.2", "xlrd==1.2.0", "tqdm==4.51.0"],
      zip_safe=False
)
