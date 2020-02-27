class CommandName(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        """
        parameters will be initialized here
        You have to reserve the vars here that you need to use
        in _vars must be the same name as handled_params in the config json but without dash (-) 
        """
        self._param1 = None
        self._param2 = None

        _vars = ['param1', 'param2']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def run(self):
        print('Command has been run arg: {}'.format(self.arg))

