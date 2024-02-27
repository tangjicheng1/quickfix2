# Quickfix2

## description
This Python package is the same as the original QuickFIX package,  
except that it is compiled binaries for Linux and macOS.  
source code: https://github.com/tangjicheng46/quickfix2  
original source code: https://github.com/quickfix/quickfix  
## build
```
pip install -U setuptools wheel twine

python setup.py bdist_wheel --plat-name=manylinux1_x86_64
```