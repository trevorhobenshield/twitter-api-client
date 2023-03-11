#!/usr/bin/bash

# import shutil;import pathlib;[shutil.rmtree(p) for p in pathlib.Path().iterdir() if p.name in {'env', 'dist', 'twitter.egg-info'}];
python3 -m build
python3 -m twine upload dist/*