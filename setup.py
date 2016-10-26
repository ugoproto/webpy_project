try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Starship Survival',
    'author': 'Ugofolio',
    'url': 'of your choice',
    'download_url': '??Where to download it.',
    'author_email': '',
    'version': '2.0',
    'install_requires': ['web'],
    'packages': ['???gothonmap'],
    'scripts': [],
    'name': 'webpy_project'
}

setup(**config)
