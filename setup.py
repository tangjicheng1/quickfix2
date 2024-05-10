from distutils.core import setup
from distutils.core import Extension
from distutils.command.install import install
from distutils.command.build import build
from distutils.command.build_ext import build_ext
from distutils.sysconfig import get_config_vars

import subprocess
import shutil
import glob
import os
import sys

class build_ext_subclass( build_ext ):
    def build_extensions(self):
        print("building quickfix2 ...")
        self.compiler.define_macro("PYTHON_MAJOR_VERSION", sys.version_info[0])
        self.compiler.define_macro("HAVE_STD_TR1_SHARED_PTR")
        self.compiler.define_macro("HAVE_STD_SHARED_PTR")
        self.compiler.define_macro("HAVE_STD_UNIQUE_PTR")
        build_ext.build_extensions(self)

# Remove the "-Wstrict-prototypes" compiler option, which isn't valid for C++.
import distutils.sysconfig
cfg_vars = distutils.sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:
        cfg_vars[key] = value.replace("-Wstrict-prototypes", "")
        
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('LICENSE') as file:
    license = file.read()

setup(name='quickfix2',
      version='1.0.0',
      py_modules=['quickfix', 'quickfixt11', 'quickfix40', 'quickfix41', 'quickfix42', 'quickfix43', 'quickfix44', 'quickfix50', 'quickfix50sp1', 'quickfix50sp2'],
      data_files=[('share/quickfix', glob.glob('spec/FIX*.xml'))],
      maintainer='tangjicheng',
      maintainer_email='tangjch15@gmail.com',
      description="FIX (Financial Information eXchange) protocol implementation; original author: Oren Miller, oren@quickfixengine.org",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license=license,
      include_dirs=['C++'],
      cmdclass = {'build_ext': build_ext_subclass },
      ext_modules=[Extension('_quickfix', glob.glob('C++/*.cpp'), extra_compile_args=['-std=c++11', '-Wno-deprecated', '-Wno-unused-variable', '-Wno-deprecated-declarations', '-Wno-uninitialized', '-static-libstdc++'], extra_link_args=["-static-libstdc++"])],
)
