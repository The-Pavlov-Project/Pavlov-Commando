class BaseCommandReader(object):

    def __init__(self):
        self.module = None  # the module where is member of
        self.name = None  # the name of the command

        self.max_invocations = None  # max uses for a single user

        self.invocation_words = None
        self.__description = None
        self.examples = None
