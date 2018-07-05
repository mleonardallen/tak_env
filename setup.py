from setuptools import setup

setup(
  name='tak_env',
  version='0.1',
  description='TAK - OpenAI Gym - Reinforcement Learning Environment',
  url='https://github.com/mleonardallen/tak_env',
  author='Mike Allen',
  author_email='mikeleonardallen@gmail.com',
  license='MIT',
  packages=['tak_env'],
  install_requires=[
    'gym',
    'pygame'
  ],
  zip_safe=False
)