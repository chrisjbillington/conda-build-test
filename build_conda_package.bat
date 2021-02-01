SET CONDA_INSTALLER=Miniconda3-latest-Windows-x86_64.exe
curl -LO https://repo.continuum.io/miniconda/%CONDA_INSTALLER%
%CONDA_INSTALLER% /S /D=%CD%\.miniconda
.miniconda\Scripts\activate
conda update -n base -c defaults conda
conda install conda-build
conda-build .
