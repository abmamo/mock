from setuptools import setup, find_packages

setup(
      name='mock',
      version='0.0.2',
      description='generate fake data',
      url='http://github.com/abmamo/mock',
      author='Abenezer Mamo',
      author_email='contact@abmamo.com',
      license='MIT',
      packages=find_packages(exclude=("tests", "env")),
      install_requires=["pandas==1.1.2", "sqlalchemy==1.3.20", "pyarrow==0.16.0", "Faker==4.14.2"],
      zip_safe=False
)
