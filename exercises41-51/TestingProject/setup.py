try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project to practice automated testing',
    'author': 'Spencer Cheney',
    'url': 'URL to get it.',
    'download_url': 'Where to download it',
    'author_email': 'spencercheney@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TestingProject'],
    'scripts': [],
    'name': 'TestingProject'
}

setup(**config)