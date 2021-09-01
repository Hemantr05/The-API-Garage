#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# explicitly config
test_args = [
    'tests'
]

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = test_args

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='IncomeAPI',
      version='0.1.0',
      description='Predict whether income exceeds $50K/yr based on census data. Also known as "Census Income" dataset. '
                  'Sklearn',
      author='Hemant Rakesh',
      author_email='hemantrak05@gmail.com',
      url='https://github.com/Hemantr05/Income-API',
      download_url='https://github.com/tflearn/tflearn/tarball/0.5.0',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'numpy',
          'six',
          'Pillow',
          'markdown',
          'djangorestframework',
          'django-filter',
          'pandas',
          'scikit-learn',
          'joblib',
          'django',
          'requests'
      ],
      test_suite='tests',
      cmdclass={'test': PyTest},
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ],
      keywords=[
          'API',
          'Django',
          'PyTorch',
          'Machine Learning',
          'Neural Networks',
          'AI'
      ]
      )
