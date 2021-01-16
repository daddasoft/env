from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='appdotenv',
    version='1.0.1',
    description='Useful tools to work with env files in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    license='MIT',
    packages=find_packages(),
    author='Hicham dadda',
    author_email='studio.dadda@gmail.com',
    keywords=['env', 'appEnv', 'web'],
    url='https://github.com/daddasoft/env',
    download_url='https://pypi.org/project/elastictools/'
)

if __name__ == '__main__':
    setup(**setup_args)
