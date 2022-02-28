try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Lucas",
    "url": "URL to get it at",
    "download_url": "Where to download it",
    "author_email": "yoshisthickass@outlook.com",
    "version": "0.1",
    "install requires": ["nose"],
    "packages": ["NAME"],
    "scripts": [],
    "name": "projectname",
}

setup(**config)
