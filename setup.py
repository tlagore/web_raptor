from setuptools import setup

setup(name='web_raptor',
      version='0.1.0',
      packages=['web_raptor'],
      entry_points={
          'console_scripts':[
              'web_raptor = web_raptor.__main__:main'
              ]
          },
      )
