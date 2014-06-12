from distutils.core import setup

setup(
    name='ElasticsearchIndex',
    version='0.1.0',
    author='Ashish Hunnargikar',
    author_email='ahunnargikar@ebay.com',
    packages=['elasticsearchindex'],
    #scripts=['bin/elasticsearchindex.py'],
    #url='http://pypi.python.org/pypi/ElasticsearchIndex/',
    license='LICENSE.txt',
    description='Elasticsearch backend search module for the Docker registry',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyelasticsearch>=0.6.1",
        "urllib2",
    ],
)