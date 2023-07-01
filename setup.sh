#!/usr/bin/bash

python -m build
python -m twine upload dist/*