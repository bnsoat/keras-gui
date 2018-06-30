@echo off
title Installing Keras-gui...
echo wait for the installation to complete 
echo y|pip uninstall keras-gui
python setup.py build 
python setup.py install

