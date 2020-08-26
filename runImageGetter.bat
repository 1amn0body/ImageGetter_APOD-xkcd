@echo off
if exist imgs (
    rmdir /q /s imgs
)

mkdir imgs
cd imgs

python ..\getXkcdComic.py
python ..\getAPOD.py
