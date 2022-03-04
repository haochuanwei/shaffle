import setuptools
import os


def get_description():
    if os.path.isfile("README.md"):
        with open("README.md", "r") as fh:
            desc = fh.read()
    else:
        desc = ""
    return desc


setuptools.setup(
    name="shaffle",
    version="0.0.1",
    description="SHA-ffle: Map hash-ables to pseudo-random numbers.",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author="Pavel",
    url="https://github.com/codestem/shaffle",
    packages=setuptools.find_packages(include=["shaffle*"]),
    install_requires=[
        # only hashlib,
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
