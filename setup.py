try:
    from setuptools import setup
    from projects import binscript
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Lucas",
    "url": "https://github.com/kyuoven/python-learning",
    "download_url": "https://github.com/kyuoven/python-learning/tree/main/projects/skeleton",
    "author_email": "yoshisthickass@outlook.com",
    "version": "0.1",
    "install requires": ["nose"],
    "packages": ["NAME"],
    "scripts": [],
    "name": "projectname",
}

setup(**config)
