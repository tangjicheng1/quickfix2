# Quickfix2

## description
same with quickfix, but build for linux and macos.


## build
```
pip install -U setuptools wheel twine

python setup.py bdist_wheel --plat-name=manylinux1_x86_64
```