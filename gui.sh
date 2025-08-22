#!/bin/sh
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPT_PATH=$(dirname "$SCRIPT")

PYTHONHOME=/home/matteo/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu
export PYTHONHOME
NUITKA_PYTHONPATH="/home/matteo/code/simulator/.venv/bin:/home/matteo/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13:/home/matteo/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/lib-dynload:/home/matteo/code/simulator/.venv/lib/python3.13/site-packages"
export NUITKA_PYTHONPATH
PYTHONPATH="/home/matteo/code/simulator/.venv/bin:/home/matteo/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13:/home/matteo/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/lib-dynload:/home/matteo/code/simulator/.venv/lib/python3.13/site-packages"
export PYTHONPATH

"$SCRIPT_PATH/gui.bin" $@

