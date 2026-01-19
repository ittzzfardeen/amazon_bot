from setuptools import find_packages,setup

setup(name="amazon_e-commerce-bot",
       version="0.0.1",
       author="fardeen",
       author_email="fardeen@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])