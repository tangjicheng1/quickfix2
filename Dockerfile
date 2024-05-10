FROM fedora:40
WORKDIR /qf2
COPY . .
RUN dnf install -y gcc-c++ libstdc++-static python3-devel python3 python3-pip
RUN pip3 install --upgrade --no-cache-dir setuptools wheel twine
RUN python3 setup.py bdist_wheel --plat-name=manylinux1_x86_64
