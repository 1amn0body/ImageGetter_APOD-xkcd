import configparser, os

osSep = os.path.sep
currDir = os.getcwd()

def readConfig(cfgName="imageGetter-cfg.ini"):
    if os.path.exists(cfgName) and os.path.isfile(cfgName):
        cfg = configparser.ConfigParser()
        cfg.read(cfgName)

        path = cfg['SAVEPATH']['path']

        if not os.path.exists(path) or os.path.isfile(path):
            try:
                os.mkdir(path)
            except Exception as e:
                print("Tried to re-create save directory but failed.")

        clearImages = cfg['IMAGES'].getboolean('clear_images')
        max_APOD = int(cfg['IMAGES']['max_apod'])
        max_xkcd = int(cfg['IMAGES']['max_xkcd'])

        savedImages = cfg['SAVED_IMAGES']['images']
        if len(savedImages) > 0: savedImages = savedImages.split(',')
        else: savedImages = []

        #remove images if clear images = True
        if len(savedImages) > 0 and clearImages:
            updateSavedImages(None, True)

        return path, max_APOD, max_xkcd, cfgName
    else:
        createConfig(cfgName)
        return readConfig()

def updateSavedImages(saveImage, clear=False, cfgName="imageGetter-cfg.ini"):
    cfg = configparser.ConfigParser()
    cfg.read(cfgName)

    path = cfg['SAVEPATH']['path']

    savedImages = cfg['SAVED_IMAGES']['images']
    if len(savedImages) > 0: savedImages = savedImages.split(',')
    else: savedImages = []

    if clear == False:
        savedImages += saveImage
        cfg['SAVED_IMAGES'] = {'images': ','.join(savedImages)}
    else:
        for i in savedImages:
            if len(i) > 0 and os.path.isfile(path + osSep + i):
                try:
                    os.remove(path + osSep + i)
                except Exception as e:
                    print("File could not be deleted.")
        # clear imagelist
        cfg['SAVED_IMAGES'] = {'images': ''}

    with open(cfgName, 'wt+') as cfgFile:
        cfg.write(cfgFile)

def createConfig(cfgName="imageGetter-cfg.ini"):
    print("Setting up your config now:")
    while True: # savepath
        path = input("Savepath for downloaded images: ").replace("/", osSep).replace("\\", osSep).replace("\n", '')

        if not os.path.isabs(path): # is absolute
            if (path != "") and (path != osSep) and (path is not None):
                if path[0] != osSep:
                    path = os.path.join(currDir + osSep + path)
                else:
                    path = os.path.join(currDir + path)
            else:
                path = os.path.join(currDir + osSep + "imgs")

        if not os.path.exists(path):
            #make dir
            try:
                os.mkdir(path)
                print("Created directory:", path)
                print()
                break
            except Exception as e:
                print("Something went wrong, please try again.")
                continue
        elif os.path.exists(path) and os.path.isfile(path):
            print("Your path is a file, please use a directory instead.")
            continue
        print("Validated that directory exists:", path)
        print()
        break
    while True: # clearImages
        try:
            clearImages = input("Clear saved images everytime at execution? (y/n): ")[0].lower()
            if clearImages == 'y' or clearImages == 'n':
                if clearImages == 'y': clearImages = "yes"
                else: clearImages = "no"
                print()
                break

            print("That was some other character, please try again.")
            continue
        except Exception as e:
            print("Something went wrong, please try again.")
            continue
    while True: # apodnum
        try:
            apodnum = int(input("Maximal image count for Astronomy Picture Of the Day (APOD): "))
            if apodnum < 0:
                apodnum = 0
            print()
            break
        except Exception as e:
            print("That was not a valid number. Try again...")
            continue
    while True: # xkcdnum
        try:
            xkcdnum = int(input("Maximal image count for xkcd-Comics: "))
            if xkcdnum < 0:
                xkcdnum = 0
            print()
            break
        except Exception as e:
            print("That was not a valid number. Try again...")
            continue

    cfg = configparser.ConfigParser() # create config object
    cfg['SAVEPATH'] = {'path': path}
    cfg['IMAGES'] = {
                    'clear_images': clearImages,
                    'max_apod': apodnum,
                    'max_xkcd': xkcdnum
                    }
    cfg['SAVED_IMAGES'] = {'images': ''}

    with open(cfgName, "wt") as cfgFile:
        cfg.write(cfgFile)
        print("Created config file:", cfgName)
        print()
