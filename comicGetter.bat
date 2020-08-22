@echo off
if exist imgs (
    rmdir /q /s imgs
)

mkdir imgs
cd imgs

python ..\getXkcdComics.py
python ..\getAstronomyPictureOfTheDay.py
