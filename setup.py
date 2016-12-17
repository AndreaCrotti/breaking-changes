from setuptools import setup


package = 'breaking_changes'

setup(name=package,
      version='0.1.0',
      packages=['breaking_changes'],
      description="Analyse different package versions for differences",
      author="Andrea Crotti",
      setup_requires=["GitPython>=2.0", "jsondiff>=0.2.0", "scandir>=1.3", "pyyaml>=3.12"],
      author_email="andrea.crotti.0@gmail.com",
      license='MIT',
      entry_points={
          'console_scripts': [
              'inspect=breaking_changes.inspector:cli',
              'compare=breaking_changes.compare:cli',
              'fetch=breaking_changes.fetch:cli',
          ],
      },
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],

      url='https://github.com/AndreaCrotti/breaking_changes')
