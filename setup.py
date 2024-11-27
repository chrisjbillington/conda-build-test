import os
from setuptools import setup, Extension

EXT_MODULES = [
    Extension(
        'conda_build_test.conda_build_test',
        sources=[os.path.join('src', 'conda_build_test.cpp')],
    )
]

setup()
