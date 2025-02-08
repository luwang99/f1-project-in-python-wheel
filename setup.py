from setuptools import setup, find_packages

#import src

setup(
  name='my_test_package',
  version='0.1',
  author='Lu L',
  url='https://databricks.com',
  author_email='lullz7025@outlook.com',
  description='my test wheel',
  packages=find_packages(),
  entry_points={
    'group_1': 'run=src.ingestion.main:main'
  },
  install_requires=[
    'setuptools'
  ]
)
