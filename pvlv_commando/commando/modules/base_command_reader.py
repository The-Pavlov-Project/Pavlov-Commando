class BaseCommandReader(object):

    def __init__(self):
        self.module = None  # the module where is member of
        self.name = None  # the name of the command

        self.max_invocations = None  # max uses for a single user

        self.invocation_words = None
        self.description = None
        self.examples = None

    @staticmethod
    def __read_value_by_language(language, dictionary):
        description = dictionary.get(language)
        if description is None:
            description = dictionary.get('eng')
            if description is None:
                raise Exception('There is not language descriptions in this command')
        return description

    def read_description_by_language(self, language):
        return self.__read_value_by_language(language, self.description)
