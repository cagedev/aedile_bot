# from thread import Board

class Chat(object):
    def __init__(self, id):
        self.id = id
        self.threads = []

    def add_board(self, uri):
        # check if valid uri
        # if true
        self.boards.append(Board(uri))
        # return succes
        # if false
        # return error

    def update_threads(self):
        for t in self.threads:
            t.update()
            msg = str(t.posts[-1])
