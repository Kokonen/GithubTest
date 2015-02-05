text = getText()
font = FontLoader().loadFont('fancyFont/')

drawer = TextDrawer()
drawer.setFont(font)
drawer.draw(text)
def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        pass

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass


t = getText()
f = FontLoader().loadFont('fancyFont/')