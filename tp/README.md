conda create -n runtprompt python=3.8 -y
conda activate runtprompt
# Python >= 3.8
# Pip >= 19.2
# .NET SDK >= 5.0
# tpromptlib >= 0.0.1.8
python -m pip install artifacts-keyring
python -m pip install tpromptlib --index-url=https://pkgs.dev.azure.com/TScience/_packaging/AIMS.TScience.NL2Code/pypi/simple/
