import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="GeoSAM-Image-Encoder",
    version="1.0.4",
    author="Joey, Fancy",
    author_email="fanchy14@lzu.edu.cn",
    description="A package for encoding satellite images into Geo-SAM features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fanchengyan/GeoSAM-Image-Encoder",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'tqdm',
        'setuptools',
        'torchgeo',
        'segment-anything'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
