#!/usr/bin/bash
wallDir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/../..
venvDir=$wallDir/run/venv
if [ ! -d "$venvDir" ]; then
  python3 -m venv $venvDir
fi
source $venvDir/bin/activate
pip3 install -r $wallDir/run/requirements.txt
python3 $wallDir/run/src/main.py
deactivate

