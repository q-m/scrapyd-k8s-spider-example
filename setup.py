from pkg_resources import parse_requirements
from setuptools import setup, find_packages

from example.version import VERSION

with open('requirements.txt', 'r') as requirements_txt:
    dependencies = [str(requirement) for requirement in parse_requirements(requirements_txt)]

setup(
    name='scrapyd-k8s-spider-example',
    version=VERSION,
    url='https://github.com/q-m/scrapyd-k8s-spider-example',
    author='wvengen',
    author_email='willem@thequestionmark.org',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = example.settings']},
    install_requires=dependencies,
)
