# -*-coding:Latin-1 -*
# /usr/bin/python3
"""module download: download the viewers file"""


def download(pseudo, loop, debug=0):
    """function download: download the viewers list file in the download folder """

    # import lib
    try:
        import shutil   # lib : write file
    except ImportError:
        raise ImportError("unable to load lib: shutil")

    try:
        import urllib.request  # lib : download the file
    except ImportError:
        raise ImportError("unable to load lib: urllib")

    # pseudo check
    if pseudo == "":
        raise ValueError("no pseudo")

    # URL and file name define
    url = "https://tmi.twitch.tv/group/user/{0}/chatters".format(pseudo)
    file_name = "download/file{0}.json".format(loop)

    # debug : print
    if debug == 1:
        print(url)
        print(file_name)

    # download and write file
    try:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except:
        raise ConnectionError("network or file path exception")


download("playoverwatch", 1)