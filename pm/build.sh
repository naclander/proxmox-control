#!/bin/bash
black *.py
rm pm.pex
pex -o pm.pex --python-shebang='/usr/bin/env python3' -D . click -e pm  

