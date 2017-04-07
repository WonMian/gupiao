from inverted import invertedAPI
import os
import config
def invertedNow():
    f = open(config.path + '/haveInverted.txt', 'a+')
    haveInvertedName = f.readlines()

    for filename in os.listdir(config.path + '/txtlistSH'):
        # for filename in filenameList:
        filename = filename.replace('.txt', '')
        if filename not in haveInvertedName:
            try:
                invertedAPI(filename)
                f.write(filename + '\n')
            except Exception, e:
                print Exception, ":", e
invertedNow()