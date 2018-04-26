class Person():
    def __init__(self, knowledge):
        self.knowledge = knowledge
        self.learned_something_new = False

    def learned_something_new(self, slide):
        if self.knowledge not in slide:
            self.knowledge += slide
            self.learned_something_new = True
        self.raise_hand()

    def raise_hand(self):
        pass