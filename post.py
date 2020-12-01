class Post:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "Title {} and content {}.".format(self.title, self.content)