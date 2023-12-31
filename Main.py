import os, argparse, subprocess
import Elements
from Fileendings import FileEndings
from TeXGenerator import TexGenerator
from pathlib import PureWindowsPath

class Main:

    def __init__(self):
        self.topLevel = []
        self.getTopLevel()
        self.sort()
        self.generateTeX()

    def getTopLevel(self):
        startFolder = os.path.join(os.getcwd(), 'TopFolder')
        self.getItemsForFolder(startFolder, self.topLevel)
        
    def getItemsForFolder(self, startFolder, listOfElements):
        dirList = self.__getSortedDirList(startFolder)
        addedPictures = []
        for index, element in enumerate(dirList):
            elementPath = os.path.join(startFolder, element)
            elementPath = PureWindowsPath(elementPath).as_posix()
            if os.path.isdir(elementPath):
                addedPictures = []
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
                addedPictures = []
                listOfElements.append(
                    Elements.Elements()
                )
                fileNameWithoutEnding = element.split('.')[:-1]
                fileNameWithoutEnding = ".".join(fileNameWithoutEnding)
                elementVals = fileNameWithoutEnding.split('--')
                listOfElements[-1].addTeX(elementPath, elementVals[0], elementVals[1])

    def addPictures(self, topFolder, fileNameList, list, addedPictures):
        while len(addedPictures) < len (fileNameList):
            element = Elements.Elements()
            counter = 0
            for index, fileName in enumerate(fileNameList):
                if fileName not in addedPictures:
                    addedPictures.append(fileName)
                    fileNameWithoutEnding = fileName.split('.')[:-1]
                    fileNameWithoutEnding = ".".join(fileNameWithoutEnding) 
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

    def sort(self):
        self.topLevel = sorted(self.topLevel, key=lambda x: x.number)
        for section in self.topLevel:
            section.sort()

    def __getSortedDirList(self, startFolder):
        dirList = os.listdir(startFolder)
        dirList = [item for item in dirList if not item.startswith("ignore--")]
        dirList = sorted(dirList, key=lambda x: self.__getItemNumber(x))
        return dirList    

    def __getItemNumber(self, path):
        filename = os.path.basename(path)
        if "--" in filename:
            return (int(filename.split('--')[0]))
        return 0


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