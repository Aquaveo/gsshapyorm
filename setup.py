import gsshapyorm
from setuptools import setup, find_packages

requires = [
    'appdirs',
    'geopandas',
    'mapkit>=1.2.6',
    'numpy',
    'pandas',
    'psycopg2',
    'sqlalchemy',
    'timezonefinder',
    'pyyaml'
]

setup(name='gsshapyorm',
      version=gsshapyorm.version(),
      description='An SQLAlchemy ORM for GSSHA model files.',
      long_description='',
      author='Nathan Swain, Alan D. Snow, and Scott D. Christensen',
      author_email='nswain@aquaveo.com',
      url='',
      license='BSD 3-Clause License',
      keywords='GSSHA, database, object relational model',
      packages=find_packages(),
      package_data={'': ['grid/land_cover/*.txt']},
      classifiers=[
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
                ],
      install_requires=requires,
      extras_require={
        'tests': [
            'coveralls',
            'pytest',
            'pytest-cov',
        ],
        'docs': [
            'mock',
            'sphinx',
            'sphinx_rtd_theme',
            'sphinxcontrib-napoleon',
        ]
      },
      )
