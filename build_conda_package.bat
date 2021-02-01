echo "setting env var"
SET CONDA_INSTALLER=Miniconda3-latest-Windows-x86_64.exe
echo "downloading conda"
curl -LO https://repo.continuum.io/miniconda/%CONDA_INSTALLER%
echo "installing conda"
%CONDA_INSTALLER% /S /D=%CD%\.miniconda
echo "activating"
.miniconda\Scripts\activate
echo "updating conda base"
conda update -n base -c defaults conda
echo "installing conda-build"
conda install conda-build
echo "building"
conda-build .
