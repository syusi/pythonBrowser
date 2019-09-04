from reader import Tag

class Perser():

    def __init__(self,reader):
        self.TagLib = {
             'html':Tag.HTML,
             'body':Tag.BODY,
             'h1':Tag.H1,
             'h2':Tag.H2
        }
        self.htmlreader = reader

    def parse(self):
        char = self.htmlreader.readOneChar()
        state = 0
        text = ''
        while state != -1:

            if state == 0:
                if char == '\n' or char == ' ' or char == '\t':
                    char = self.htmlreader.readOneChar()

                elif char == '<':
                    state = 1
                else:
                    self.htmlreader.backChar(char)
                    state = 3
            
            else if state == 1:
                char = self.htmlreader.readOneChar()
                if char == '/':
                    state = 3
