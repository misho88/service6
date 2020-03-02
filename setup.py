from setuptools import setup, find_packages
setup(
    name='service6',
    version='0.1',
    description='wrapper for s6 service utilities',
    scripts=['service6'],
    packages=find_packages(),
    author='Mihail Georgiev',
    author_email='misho88@gmail.com',
)
