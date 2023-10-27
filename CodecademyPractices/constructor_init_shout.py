class Shout:
    """A class that prints in uppercase whatever is passed at the instance"""
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper())


phrase_1 = Shout("shout")
phrase_2 = Shout("shout")
phrase_3 = Shout("let it all out!")
