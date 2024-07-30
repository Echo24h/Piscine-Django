#! /usr/bin/bash

pip --version

pip install --force-reinstall --target=./local_lib git+https://github.com/jaraco/path.git > my_script.log 2>&1

# Vérifier si l'installation a réussi
if [ $? -eq 0 ]; then
    echo "path.py has been successfully installed."
    # Exécuter le programme Python
    python3 my_program.py
else
    echo "Failed to install path.py. Check the log file for details."
fi