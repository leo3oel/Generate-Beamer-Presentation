class Section:
    
    def __init__(self, name, number, path) -> None:
        self.name = name
        self.number = int(number)
        self.elements = []
        self.path = path
        self.type = "Section"

    def sort(self):
        self.elements = sorted(self.elements, key=lambda x: x.number)
        for element in self.elements:
            element.sort()

class Elements:

    def __init__(self) -> None:
        self.type = None
        self.pictures = []
        self.length = 0
        self.number = 0

    def addPicture(self, pathToPicture, number, title, caption=None):
        self.number = int(number)
        self.title = title
        self.type = "Pictures"
        self.pictures.append(
            Picture(pathToPicture, number, caption)
        )
        self.length += 1
    
    def addTeX(self, path, number, title):
        self.number = int(number)
        self.path = path
        self.title = title
        self.type = 'TeX'
        self.length = 1
    
    def sort(self):
        self.pictures = sorted(self.pictures, key=lambda x: x.number)

class Picture():

    def __init__(self, path, number, caption) -> None:
        self.path = path
        self.number = number
        if caption:
            self.caption = caption
        else:
            self.caption = None