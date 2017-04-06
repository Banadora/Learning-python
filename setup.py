################### Labyrinthe - Exe setup ###################

# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(options={"py2exe": {
                        "packages": ["PIL"],  # For everything
                        "includes": ["PIL.Image", "PIL.PngImagePlugin"]}},windows=['Main.py']) # Or here for bits and pieces
