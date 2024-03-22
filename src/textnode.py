class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            return True
        else:
            return False

    def __repr__(self):
        return("TextNode(" + self.text + ", " + self.text_type + ", " + self.url + ")")
