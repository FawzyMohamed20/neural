from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Simple interface for working with intents and chatbots.'
LONG_DESCRIPTION = 'Simple interface for working with intents and chatbots.'

setup(
    name="Fawzy",
    version=VERSION,
    author="FawzyMohamed (AI Eng)",
    author_email="<fawzymohamed2099@gmail.com.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'nltk', 'tensorflow'],
    keywords=['python', 'neural', 'machine learning', 'chatbots', 'chat', 'artificial intelligence', 'virtual assistant'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)