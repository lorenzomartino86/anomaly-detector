from setuptools import setup, find_packages

# Default version
__version__ = '1.0.0'

# Get the correct version from file
try:
    import version
    __version__ = version.__version__
except ImportError:
    pass

setup(
    name='anomaly-detector',
    version=__version__,
    description='Anomaly detector written in Python',
    long_description='Anomaly detector written in Python',
    url='',
    author='Lorenzo Martino',
    author_email='',

    keywords='anomaly detector',

    packages=find_packages('src'),
    package_dir={'': 'src'}, include_package_data=True,
    test_suite='test'
)
