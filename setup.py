import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()


version = '1.0'


setup(name='nose-skipreq',
      version=version,
      description='nose plugin that will skip Google API RequestError exceptions.',
      long_description=README,
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.4',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Testing'],
      keywords='nose nosetest skip RequestError',
      author='Tom Davis',
      author_email='tom@recursivedream.com',
      url='https://github.com/tdavis/nose-skipreq',
      license='BSD License',
      zip_safe = False,
      py_modules = ['skipreq'],
      entry_points = {
        'nose.plugins': [ 'skipreq = skipreq:SkipRequestError' ]
      },
     )
