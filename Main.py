import os, argparse, subprocess
import Elements
from Fileendings import FileEndings
from TeXGenerator import TexGenerator
from pathlib import PureWindowsPath

class Main:

    def __init__(self):
        self.topLevel = []
        self.getTopLevel()
        self.generateTeX()

    def getTopLevel(self):
        startFolder = os.path.join(os.getcwd(), 'TopFolder')
        self.getItemsForFolder(startFolder, self.topLevel)
        
    def getItemsForFolder(self, startFolder, listOfElements):
        dirList = os.listdir(startFolder)
        addedPictures = []
        for index, element in enumerate(dirList):
            elementPath = os.path.join(startFolder, element)
            elementPath = PureWindowsPath(elementPath).as_posix()
            if os.path.isdir(elementPath):
                folderVals = element.split('--')
                listOfElements.append(
                    Elements.Section(
                    name=folderVals[1],
                    number=folderVals[0],
                    path=elementPath
                    )
                )
                self.getItemsForFolder(elementPath, listOfElements[-1].elements)
            elif any(elementPath.lower().endswith(ending) for ending in FileEndings.pictures):
                filenameList = []
                for pictureIndex in range(index,len(dirList)):
                    if any(dirList[pictureIndex].lower().endswith(ending) for ending in FileEndings.pictures):
                        filenameList.append(dirList[pictureIndex])
                    else:
                        break
                self.addPictures(startFolder, filenameList, listOfElements, addedPictures)
            elif elementPath.lower().endswith(FileEndings.tex):
                listOfElements.append(
                    Elements.Elements()
                )
                fileNameWithoutEnding = element.split('.')[0]
                elementVals = fileNameWithoutEnding.split('--')
                listOfElements[-1].addTeX(elementPath, elementVals[0], elementVals[1])

    def addPictures(self, topFolder, fileNameList, list, addedPictures):
        while len(addedPictures) < len (fileNameList):
            element = Elements.Elements()
            counter = 0
            for index, fileName in enumerate(fileNameList):
                if fileName not in addedPictures:
                    addedPictures.append(fileName)
                    fileNameWithoutEnding = fileName.split('.')[0]
                    pictureVals = fileNameWithoutEnding.split('--')
                    fullPath = os.path.join(topFolder, fileName)
                    fullPath = PureWindowsPath(fullPath).as_posix()
                    element.addPicture(fullPath, pictureVals[0], pictureVals[1], pictureVals[3])
                    counter +=1
                    if counter == int(pictureVals[2]):
                        break
                    if len(fileNameList)-1>index:
                        if not self.__nextSlideSameTitle(fileNameList, index):
                            break
            list.append(element)

    def __nextSlideSameTitle(self, fileNameList, index):
        titleFirstSlide = fileNameList[index].split('--')[1]
        titleSecondSlide = fileNameList[index+1].split('--')[1]
        if titleFirstSlide != titleSecondSlide:
            return False
        return True

    def generateTeX(self):
        #ToDo change template to allow toplevel files
        sections = [element for element in self.topLevel if type(element) == Elements.Section]
        texGen = TexGenerator(sections)

    def compileLua(self):
        subprocess.run(["lualatex", "output.tex"])
        subprocess.run(["lualatex", "output.tex"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a LaTeX Beamer Presentation from the folder structure located in TopFolder.")
    parser.add_argument('--compileLuaLaTeX', dest="lualatex", action="store_true", help="Set this to compile the generated TeX File with LuaLaTeX")
    args = parser.parse_args()

    main = Main()

    if args.lualatex:
        main.compileLua()