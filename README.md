# Quickfix2

## description
This Python package is the same as the original QuickFIX package,  
except that it is compiled binaries for Linux and macOS.  
source code: https://github.com/tangjicheng1/quickfix2  
original source code: https://github.com/quickfix/quickfix  

## build
```
# For Linux
pip install -U setuptools wheel twine
python setup.py bdist_wheel --plat-name=manylinux1_x86_64
```

```
# For macos
python setup.py bdist_wheel
```

### install
```
# after building, you will see the wheel package in the ./dist
pip install ./dist/quickfix2-1.0.0-cp312-cp312-macosx_11_0_arm64.whl
```