import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GOSH-FHIR-2020-SAMI-AL-ALAWI",
    version="0.0.1",
    author="Sami Al Alawi",
    description="package that creates pdf files and word documents from FHIR JSON records",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="need to fill later",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: AGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
