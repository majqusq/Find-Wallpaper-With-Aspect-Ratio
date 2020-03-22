import os
from PIL import Image #pip install Pillow 

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    # Image extensions you want to use
    file_extension = ['jpg','png','peg']##Need to find better way to do this
    allFiles_nostart = []
    for i in allFiles:     
        if i[-3:] in file_extension:
            allFiles_nostart.append(i)
    return allFiles_nostart          
def get_proportions():
    wallpaper = []
    file_list = getListOfFiles('.')
    for i in list(file_list):
        try:
            img = Image.open(i)
            width, height = img.size
            # Down below you can change the division numbesr with aspect ratio you want
            w  = width/16
            h  = height/9
            img.close()
            if w == h:
                wallpaper.append(i)
            else:
                continue
        # Most probably not all errors that can occur
        except Image.DecompressionBombError:
            print('Image.DecompressionBombError','  of  ',i)
        except Image.UnidentifiedImageError:
            print('UnidentifiedImageError','  of  ',i)
    return wallpaper
    
if __name__ == '__main__':
    ## Should made this into file rather than printing out on shell
    right_proportion = get_proportions()
    for item in right_proportion:
        print(item[2:])
    os.system('pause')
    

