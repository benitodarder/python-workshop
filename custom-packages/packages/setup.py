import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="custom-package-benito-darder",
    version="0.0.1",
    author="Benito Darder",
    author_email="benitodarder@<email server>",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benitodarder/python-workshop",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Unlicense License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
