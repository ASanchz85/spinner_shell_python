from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name='terminal_spinner',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='Antonio Sánchez',
    description='A simple terminal spinner for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ASanchz85/spinner_shell_python',
)
