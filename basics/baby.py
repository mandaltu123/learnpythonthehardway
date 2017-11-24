class Baby:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print("{} is crying ".format(self.name))

    def laugh(self):
        print("{} is laughing".format(self.name))

    def hi(self):
        print("{} is saying hi!".format(self.name))