# imageGetter_APOD-xkcdComic
This project is used to download the <a href="http://apod.nasa.gov/">Astronomic Picture of the Day (APOD)</a> and the newest Comic from <a href="http://xkcd.com/"> xkcd</a>. But you can download older ones too. To change the number there are loops in the files <a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/getXkcdComic.py">getXkcdComic.py</a> and <a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/getAPOD.py">getAPOD.py</a>.

The batch (<a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/runImageGetter.bat"> Batch for python files</a>, <a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/dist/runImageGetter.bat">Batch for .exe file</a>) creates the image folder, runs the <a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/dist/runImageGetter.exe">.exe</a> (or the <a href="https://github.com/1amn0body/imageGetter_APOD-xkcdComic/blob/master/runImageGetter.py">runImageGetter.py</a>) and downloads the pictures into the folder.
The image folder is removed everytime the batch is run. SO DONT CHANGE THE PATH TO ONE WITH IMPORTANT FILES AND/OR FOLDERS!

A sript to set up the Task Scheduler under Windows is not supported right now, but hopefully will be added in future.

The executable .exe file is built with <a href="http://www.pyinstaller.org/" target="_blank">PyInstaller</a>.
Other platform releases will ma ybe added in the future.
