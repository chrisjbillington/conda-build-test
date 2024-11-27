import os
from setuptools import setup, find_packages, Extension

EXT_MODULES = [
    Extension(
        'hello.hello',
        sources=[os.path.join('src', 'hello.c')],
    )
]

setup(
    name="hello",
    version="0.1.0",
    description="hello",
    packages=find_packages(),
    ext_modules=EXT_MODULES,
)
