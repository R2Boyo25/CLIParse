from .plugins import getHandlers, loadPlugins

class Loader:
    def __init__(self, parser, directory = "commands"):
        self.parser = parser
        self.handlers = getHandlers(loadPlugins(directory))
        try:
            self.handlers["load"]
        except:
            pass
        else:
            for loader in self.handlers["load"]:
                loader(self)

    def add(self, function, name, help = ""):
        self.parser.command(name, help)(function)
