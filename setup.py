""" CNS Python based ORM Implementation (base library)
"""
from setuptools import setup, find_packages


cfg = {
    'name'             : 'cns-orm-common',
    'long_description' : __doc__,
    'version'          : '1.0.0',
    'packages'         : find_packages('src'),
    'package_dir'      : {'': 'src'},

    'namespace_packages': [
        'cns'
    ],

    'install_requires': [
        'sqlalchemy >= 1.0.9'
    ],

    'dependency_links' : [],
    'zip_safe'         : False
}


if __name__ == '__main__':
    setup(**cfg)
