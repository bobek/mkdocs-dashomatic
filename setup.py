from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-dashomatic',
    version='0.1.2',
    description='A MkDocs plugin to convert hyphens to dashes.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs markdown dash em en',
    url='https://github.com/bobek/mkdocs-dahsomatic',
    author='Antonin Kral',
    author_email='hello@bobek.cz',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-dashomatic=mkdocs_dashomatic.plugin:ContentFilterPlugin',
        ]
    }
)
