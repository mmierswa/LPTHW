try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Myles Mierswa',
    'url': 'the url',
    'download_url': 'download url',
    'author_email': 'myles.mierswa@test.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
