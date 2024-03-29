try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Scans through a sentence and seperates the roads into predefine lexicon tuples',
    'author': 'Spencer Cheney',
    'url': 'URL to get it.',
    'download_url': 'Where to download it',
    'author_email': 'spencercheney@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['WordScanner'],
    'scripts': [],
    'name': 'WordScanner'
}

setup(**config)