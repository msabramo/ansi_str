import os
from setuptools import setup

version = '0.0.0'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='ansi_str',
    version=version,
    description='Experimental Python str subclass, '
                'whose __len__ method excludes ANSI color escape codes',
    long_description=read('README.rst'),
    url='https://github.com/msabramo/ansi_str',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    py_modules=['ansi_str'],
    zip_safe=False,
    install_requires=[],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
