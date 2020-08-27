@echo off
if exist imgs (
    rmdir /q /s imgs
)

mkdir imgs
cd imgs

python ..\runImageGetter.py
