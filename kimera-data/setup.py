"""
    Packaging Python Projects
    Documentation: https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name="kimera_data",
    version="0.0.1",
    author="Ismael Antonio Sarmiento Barberia",
    author_email="ismaelantonio.sarmiento@gmail.com",
    description="Project that collects data tools in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ismael-sarmiento/kimera-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 1 - Planning"
    ],
    install_requires=REQUIREMENTS,
    python_requires='>=3.6',
)
