"""
    Packaging Python Projects
    Documentation: https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kimera_data",  # Replace with your own username
    version="0.0.1",
    author="Ismael Antonio Sarmiento Barberia",
    author_email="ismaelantonio.sarmiento@gmail.com",
    description="Project that collects data utility tools in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ismael-sarmiento/kimera-db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
