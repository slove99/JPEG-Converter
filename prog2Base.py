from wand.image import Image
import os

scanDir = "//192.168.1.82/Public\Samuel/EAC flac files"
storeDir = "C:/Users/Samuel/Desktop/Converted"

for dirpath, dirs, files in os.walk(scanDir):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        if filename == "folder.jpg":
            #print(fname)
            with Image(filename=fname) as i:
                print(i.width)
                if(i.interlace_scheme == 'jpeg'):
                    i.interlace_scheme = 'no'
                    saveName = os.path.relpath(fname, start=scanDir)
                    saveName = saveName.replace('\\', '-')
                    print(saveName)
                    saveLoc = os.path.join(storeDir, saveName)
                    i.save(filename=saveLoc)
                #with i.convert('jpg') as converted:
                    #converted.interlace_scheme = 'no'
                 #   converted.save(filename='test.jpg')
        #with open(fname) as myfile:
        #    print(myfile.name)