try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '??',
    'author': 'Spencer Cheney',
    'url': 'URL to get it.',
    'download_url': 'Where to download it',
    'author_email': 'spencercheney@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Sentences'],
    'scripts': [],
    'name': 'Sentences
}

setup(**config)