# ImageGetter_APOD-xkcd

This project is used to download the [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/) and the latest Comic from [xkcd](https://xkcd.com/). But you can download older ones too.

The config file *imageGetter-cfg.ini* is created at the first start. The following settings are available:
1. Custom storage path
2. Auto-remove of files (only the downloaded ones)
3. Custom number of image downloads (APOD, xkcd separately)

Please follow the console instructions for setting them up.

A [script to set up the Task Scheduler under Windows](https://github.com/1amn0body/ImageGetter_APOD-xkcd/blob/master/TaskSchedulerSetup.bat)(Please help me with it!) is not supported right now, but hopefully will be added in future.

The executable .exe file is built with [PyInstaller](https://www.pyinstaller.org/).
Other platform releases may be added in the future.
