from setuptools import setup, find_packages


package = 'breaking_changes'

setup(name=package,
      version='0.1.0',
      packages=['breaking_changes'],
      description="Deprecation decorator",
      author="Andrea Crotti",
      setup_requires=["GitPython>=2.0", "jsondiff>=0.2.0", "scandir>=1.3", "pyyaml>=3.12"],
      author_email="andrea.crotti.0@gmail.com",
      license='MIT',
      entry_points={
          'console_scripts': ['breaking-changes=breaking_changes:main'],
      },
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/breaking_changes')
