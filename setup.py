from setuptools import setup, find_packages

setup(
      name='mock',
      version='0.0.1',
      description='generate fake data',
      url='http://github.com/abmamo/fs2db',
      author='Abenezer Mamo',
      author_email='contact@abmamo.com',
      license='MIT',
      packages=find_packages(exclude=("tests", "env")),
      install_requires=["pandas", "fastparquet", "sqlalchemy", "pyarrow", "Faker"],
      zip_safe=False
)
