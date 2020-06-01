# Packaging Python Projects

## Documentation

* [Reference link](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)


## Pipeline
```bash
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --user --upgrade twine
python -m twine upload --repository testpypi dist/*
```