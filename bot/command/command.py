class Command:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def getUsage(self):
        return '/' + self.name + ' ' + ' '.join(self.args)