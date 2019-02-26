import re

class Post(object):

    # ? : Pass a BS4 object and parse it here?

    def __init__(self, id, num, author, content, text):
        self.id = id
        self.num = num
        self.author = author
        self.content = content
        self.text = text

    def __str__(self):
        return '['+self.id+'] #' + self.num + ': ' + re.sub('\n+', '\n', self.text.strip())
