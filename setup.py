#!/usr/bin/env python

from distutils.core import setup


setup(name='kakasi-utils',
      version='0.1',
      description='KAKASI Utilities',
      author='Yusuke Miyazaki',
      author_email='miyazaki.dev@gmail.com',
      url='https://github.com/403JFW/kakasi-utils',
      packages=['kakasi_utils'],
      scripts=['scripts/pykanwa'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities'
      ])
