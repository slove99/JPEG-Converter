from wand.image import Image
import os

scanDir = "E:/Users/Samuel/Music/EAC flac files"
storeDir = "E:/Users/Samuel/Pictures/ConvertedImages"

unconvertedImageCount = 0
totImageCount = 0
percentConverted = 0

for dirpath, dirs, files in os.walk(scanDir):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if ".jpg" in filename:
            with Image(filename=fname) as i:
                print(i.width)
                totImageCount += 1
                if(i.interlace_scheme == 'jpeg'):
                    i.interlace_scheme = 'no'
                    saveName = os.path.relpath(fname, start=scanDir)
                    saveName = saveName.replace('\\', '-')
                    print(saveName)
                    saveLoc = os.path.join(storeDir, saveName)
                    i.save(filename=saveLoc)
                    unconvertedImageCount += 1
if totImageCount > 0:
    percentConverted = (unconvertedImageCount / totImageCount) * 100
print("Found %d interlaced images out of %d images \n %f%% images converted" % (unconvertedImageCount, totImageCount,
                                                                               percentConverted))
