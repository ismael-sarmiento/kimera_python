"""
    Packaging Python Projects
    Documentation: https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kimera_core",
    version="0.0.12",
    author="Ismael Antonio Sarmiento Barberia",
    author_email="ismaelantonio.sarmiento@gmail.com",
    description="Project that collects core utility tools in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ismael-sarmiento/Kimera/tree/master/kimera-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 1 - Planning"
    ],
    python_requires='>=3.6',
)
