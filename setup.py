from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processor",
    version="0.1.0",
    author="Alex Silva",
    author_email="alex.paulo100@gmail.com",
    description="Python package to perform various image processing tasks",
    url="https://github.com/alexpaulo100/image-processing.git",
    packages=find_packages(),
    python_requires='>=3.12',

)
