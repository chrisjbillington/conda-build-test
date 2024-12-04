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
    use_scm_version=True,
    description="hello",
    packages=find_packages(),
    ext_modules=EXT_MODULES,
)
