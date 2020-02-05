from .translations.manual_reply import (
    invocation, beta, handled_args, handled_params, command_mask
)


class Manual(object):
    """
    """

    def __init__(self, language, commands_descriptor, arg, params):

        self.language = language
        self.commands_descriptor = commands_descriptor
        self.arg = arg

    def __build_title(self, command):
        _out = '**{}**\n{}\n'.format(
            command.name.upper(),
            command.description,
        )
        if command.invocation_words:
            _out += '{}\n'.format(
                invocation(self.language, command.invocation_words)
            )
        if command.beta_command:
            _out += '\n{}\n'.format(
                beta(self.language)
            )
        return _out

    def __build_args_params_list(self, title_function, dictionary):
        if dictionary != {}:
            out = '\n{}\n'.format(title_function(self.language))
            for key in dictionary.keys():
                key_description = dictionary.get(key)
                out += '**{}** -- {}\n'.format(
                    key if key != '' else 'void',
                    key_description
                )
            return out
        else:
            return ""

    def _build_full_man(self, command):

        try:
            out = self.__build_title(command)
            out += self.__build_args_params_list(handled_args, command.handled_args)
            out += self.__build_args_params_list(handled_params, command.handled_params)
            return out

        except Exception as e:
            print(e)
            return e

    def __build_base_man(self, command):

        try:
            if not command.permissions >= 100:
                return self.__build_title(command)
            else:
                return ""
        except Exception as e:
            print(e)

    def __print_found_command(self, command):
        try:
            out = '{}\n'.format(
                self.__build_title(command),
                # command_mask(self.language, '.', command, command_function.sub_call)
            )
            return out

        except Exception as e:
            print(e)
            return e

    def command_name(self):

        _out = ''
        command_found = None
        for command in self.commands_descriptor:
            if self.arg in command.invocation_words:
                command_found = command

        if command_found is None:
            return 'Command not found'

        _out = self.__print_found_command(command_found)

        return _out

    def void_arg(self):
        _out = ''
        for command in self.commands_descriptor:
            if command.name == 'manual':
                return self._build_full_man(command)

    def all_commands(self):
        _out = ''
        for command in self.commands_descriptor:
            _out += '{}\n'.format(self.__build_base_man(command))

        """
        for key in self.cr.shortcuts.shortcuts_keys:
            _out += '{}\n'.format(self._build_base_man(self.cr.shortcuts, key))
        """
        return _out

    def run(self):

        chose = {
            None: self.void_arg,
            'all': self.all_commands,
        }

        try:
            out = chose[self.arg]()
        except Exception as e:
            out = self.command_name()
            print(e)

        return out
