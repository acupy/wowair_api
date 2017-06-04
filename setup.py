from setuptools import setup

def long_description():
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
  name = 'wowair',
  packages = ['wowair'],
  version = '0.4',
  license='MIT',
  description = 'WowAir Python API',
  long_description=long_description(),
  author = 'Adam Czuprak',
  author_email = 'adam.czuprak@hotmail.com',
  url = 'https://github.com/acupy/wowair_api',
  download_url = 'https://github.com/acupy/wowair_api/archive/0.4.tar.gz',
  install_requires=['requests'],
  keywords = ['wowair', 'api'],
  classifiers = [],
)
