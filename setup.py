from setuptools import setup, find_packages
from distutils.spawn import find_executable
from pathlib import Path
from subprocess import run

for browser in ('w3m', 'lynx', 'links'):
    if find_executable(browser):
        break
else:
    raise RuntimeError("need w3m, lynx or links to make help docs")

for path in Path('.').glob('s6*/doc/s6*.html'):
    res = run([ browser, '-dump', str(path) ], capture_output=True, check=True)
    outpath = Path('service6doc/doc') / path.stem
    outpath.write_bytes(res.stdout)

setup(
    name='service6',
    version='0.1',
    description='wrapper for s6 service utilities',
    scripts=['service6'],
    packages=['service6doc'],
    author='Mihail Georgiev',
    author_email='misho88@gmail.com',
    package_data={
        'service6doc': ['doc/*'],
    }
)
