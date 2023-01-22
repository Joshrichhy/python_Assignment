class Animal:
    # def __init__(self):
    #     self.name = None
    #     self.speak = None
    #     self.dance = None

    def __init__(self, name, speak, dance, run):
        self.name = name
        self.speak = speak
        self.dance = dance
        self.run = run
        self.food = []

    def set__animal_name(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def set_animal_speak(self, lang):
        self.speak = lang

    def get_speak(self):
        return self.speak

    def set_animal_dance(self, dance_move):
        self.dance = dance_move

    def get_dance(self):
        return self.dance

    def set_run(self, value):
        self.run = value
        if self.run:
            print("1000 meter")
        else:
            print("cant run")

    def can_run(self):
        return self.run

    def set_food(self, *args):
        # for i in range(len(args)):
        #     self.food.append(args[i])
        self.food = [i for i in args]
        print(len(args))

    def get_food(self):
        return self.food


