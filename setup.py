from setuptools import setup

setup(
    name='mem_restrict',
    version='0.1.0',
    description='Restrict memory usage, specifically useful for preventing ssh-server killed by linux oom',
    url='https://github.com/daniel-redder/mem_restrict',
    author='Daniel Redder',
    packages = ['mem_restrict'],
)