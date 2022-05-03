# kimera-python

Project that collects utility tools in python.

# Tools

### Environment

* **[virtualenv](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3)**:
    * install virtualenv package via pip: `pip install virtualenv`
    * create virtualenv: `virtualenv -p python3 <project_name>`
* **requirements**:
    *
    install [requirements file](https://programmerclick.com/article/96431530449/): `pip install -r /path/to/requirements.txt`
* **[tox]((https://coffeebytes.dev/por-que-usar-tox/))**
    * create [tox.ini](https://tox.wiki/en/latest/examples.html) by answer: `tox-quickstart`
    * run:`tox`

### [Package]((https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects))

* Pipeline:
  ```bash
  python -m pip install --upgrade setuptools wheel
  python setup.py sdist bdist_wheel
  python -m pip install --upgrade twine
  python -m twine upload --repository testpypi dist/*
  pip install -i https://test.pypi.org/simple/ kimera-<NAME>
  ```