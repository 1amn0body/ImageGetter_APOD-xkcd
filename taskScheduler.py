import platform, distro

def setupScheduler():
    operatingSystem = platform.system().lower()

    if operatingSystem == "windows": # setup for windows
        print("Setting up Task Scheduler for Windows...")

    elif operatingSystem == "linux": # setup for linux
        print("Trying to set up Task Scheduler for Linux...")

        baseDist = distro.like().lower()
        if len(baseDist) < 1: baseDist = distro.id().lower()
        #print(baseDist)

        if baseDist == "debian":
            pass

        elif baseDist == "arch":
            pass

        elif baseDist == "gentoo":
            pass

        elif baseDist == "fedora":
            pass

        elif baseDist == "opensuse":
            pass

        elif baseDist == "rhel":
            pass

        elif baseDist == "ubuntu":
            pass

        elif baseDist == "solaris":
            pass

    elif baseDist == "freebsd":
            pass

    #elif baseDist == "slackware":
    #    pass

        else:
            print("Unable to detect the Linux base distribution or it is unknown.\nPlease set up a task scheduler yourself.")

    elif operatingSystem == "darwin": # setup for mac
        print("Setting up Task Scheduler for Mac...")
        pass

    else:
        print("Unable to detect OS.\nPlease set up a task scheduler yourself.")
