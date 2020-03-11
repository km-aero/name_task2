class NewUsers:
    def __init__(self, name):
        self.name = name

    def create_info_file(self):
        with open(self.name + '.txt', 'a+') as f:
            f.write('Name: ' + self.name.)