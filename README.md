# ImageGetter_APOD-xkcd



This project is used to download the [Astronomic Picture of the Day (APOD)](http://apod.nasa.gov/) and the latest Comic from [xkcd](http://xkcd.com/). But you can download older ones too. To change the number there are loops in the files [getXkcdComic.py](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/getXkcdComic.py) and [getAPOD.py](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/getAPOD.py).

The batch ([Batch for .exe file](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/dist/runImageGetter.bat), [Batch for python files](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/runImageGetter.bat)) creates the image folder, runs the [.exe](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/dist/runImageGetter.exe) (or the [runImageGetter.py](https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/runImageGetter.py)) and downloads the pictures into the folder.
The image folder is removed everytime the batch is executed.<br>
**SO DONT CHANGE THE PATH TO ONE WITH IMPORTANT FILES AND/OR FOLDERS!**

A script to set up the Task Scheduler under Windows is not supported right now, but hopefully will be added in future.

The executable .exe file is built with [PyInstaller](http://www.pyinstaller.org/).
Other platform releases may be added in the future.
