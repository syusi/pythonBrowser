from enum import IntEnum,auto

class Tag(IntEnum):
    HTML = auto()
    BODY = auto()
    H1 = auto()
    H2 = auto()


class Reader():

    def __init__(self,source):
        self.htmlSource = source
        if self.htmlSource == None:
            self.htmlSource = open('./index.html','r',encoding='UTF-8')

        self.content = list(self.htmlSource.read())
        self.htmlSource.close()

        self.backCharacter = None

    def readOneChar(self):
        char = None

        if len(self.content) == 0:
            return char

        if self.backCharacter == None:
            char = self.content[0]
            del self.content[0]
        else:
            char = self.backCharacter
            self.backCharacter = None

        return char

    def backChar(self,char):
        self.backCharacter = char




if __name__ == "__main__":
    textReader = Reader(None)

    while True:
        char = textReader.readOneChar()
        if char == None:
            break
        print(char,end = ',')