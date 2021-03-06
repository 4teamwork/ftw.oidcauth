from setuptools import setup, find_packages
import os

version = '1.0.3.dev0'

tests_require = [
    'mock',
    'plone.app.testing',
]

setup(name='ftw.oidcauth',
      version=version,
      description="A PAS plugin for authentication of users in Plone using OIDC.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: 5.1',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='4teamwork AG',
      author_email='info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.oidcauth',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Plone',
          'PyJWT',
          'cryptography',
          'plone.api',
          'requests',
          'setuptools',
          'six',
      ],
      tests_require=tests_require,
      extras_require={
          'tests': tests_require,
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
