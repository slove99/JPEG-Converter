from wand.image import Image
import os

scanDir = "" # Path containing images to convert
storeDir = "" # Path to store converted images

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
                    # Format source directory into output file name
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
