# This is the first class


class Stuff(object):

    def __init__(self, name):
        self.name = name;



    def printname(self):
        print("The name is {}".format(self.name))


def main():
    stuffone = Stuff("jimmy page")
    stufftwo = Stuff("angus young")
    stuffone.printname()
    stufftwo.printname()


if __name__ == '__main__':
    main()
