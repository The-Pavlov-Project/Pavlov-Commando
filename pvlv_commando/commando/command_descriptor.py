import json
from pvlv_commando.commando.modules.base_command_reader import BaseCommandReader


class CommandDescriptor(BaseCommandReader):

    def __init__(self):
        super(CommandDescriptor, self).__init__()

        self.management_command = None  # can be used only by owner of the bot

        self.beta_command = None
        self.pro_command = None  # payment command, set the level of pro 1, 2, 3, etc.
        self.dm_enabled = None  # can be used also in dm
        self.enabled_by_default = None  # this command is active by default
        self.permissions = None  # permissions to use the command

        self.handled_args = None
        self.handled_params = None

    def read_arg_by_language(self, language, dictionary):
        result = {}
        for key in dictionary.keys():
            result[key] = self.__read_value_by_language(language, dictionary.get(key))
        return result

    def read_command(self, command_descriptor_dir):

        with open(command_descriptor_dir) as f:
            file = json.load(f)

        self.management_command = file.get('management_command')
        self.beta_command = file.get('beta_command')
        self.pro_command = file.get('pro_command')
        self.dm_enabled = file.get('dm_enabled')
        self.enabled_by_default = file.get('enabled_by_default')
        self.permissions = file.get('permissions')
        self.invocation_words = file.get('invocation_words')

        self.description = file.get('description')
        self.handled_args = file.get('handled_args')
        self.handled_params = file.get('handled_params')

        self.examples = file.get('examples')

    @property
    def handled_args_list(self):
        return self.handled_args.keys()

    @property
    def handled_params_list(self):
        return self.handled_params.keys()
