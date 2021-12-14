from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Convert Number to Bangla Word Text'
LONG_DESCRIPTION = 'A package that allows number input and convert the number as bangla word text .'

# Setting up
setup(
    name="number2bangla_word_text",
    version=VERSION,
    author="Md. Nazmul Hossain",
    author_email="<nazmul.cse48@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/MdNazmul9/number2bangla_word_text",
    packages=find_packages(),
    install_requires=[],
    keywords=['python3','number2bangali-word-text','number2word-text','number-to-bangali-word-text','number-to-word-text','number-to-bangla-text' ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ]
)
