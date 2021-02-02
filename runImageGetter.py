import getXkcdComic, getAPOD, configCreator

path, max_APOD, max_xkcd, cfgName = configCreator.readConfig()
imgs = []

print("Downloading...")
imgs += getAPOD.runGetter(path, max_APOD)
imgs += getXkcdComic.runGetter(path, max_xkcd)

configCreator.updateSavedImages(imgs, cfgName=cfgName)

"""************************************************
* currently using TaskScheduler_Windows as branch *
************************************************"""
