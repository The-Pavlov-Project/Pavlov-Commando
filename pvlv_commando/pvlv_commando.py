import os
import logging
from pvlv_commando.commando.command_importer import importer, build_descriptor
from pvlv_commando.commando.command_descriptor import CommandDescriptor
from pvlv_commando.manual.manual import Manual


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pvlv_command')

"""
fh = logging.FileHandler('logs/pvlv_command.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
"""


class Commando(object):
    def __init__(self):
        """
        Load all the packages and commands should be done only once.
        For efficiency it must be put as a static class for all the project.
        """
        self.__command_list = importer()

        """
        Structure of the command found
        Stored to be executed
        """
        self.__command_found = None
        self.error = ''
        self.language = 'eng'
        self.trigger = None
        self.arg = None
        self.params = {}

        # Builtin manual
        self.__is_manual = False

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.__manual = build_descriptor('builtin', 'manual', dir_path + '/manual/manual.json')

        self.__command_list.append((self.__manual, None, None))

    def find_command(self, text: str, language: str):
        """
        Find if there is a command in the text
        N.B.: YOU HAVE TO REMOVE THE COMMAND CHAR/STR TRIGGER AND SEND CLEAN TEXT

        :param text: the message without the chat/str command invocation
        :param language: the language code for message response
        :return: True if there is a command else False
        """
        self.language = language

        self.__read_command_structure(text)

        for command in self.__command_list:
            command_descriptor, module, class_name = command
            if self.trigger in command_descriptor.invocation_words:
                self.__command_found = command

                if self.__manual == command_descriptor:
                    self.__is_manual = True
                return

        self.error = 'Command not found'
        raise Exception

    @property
    def command(self):
        """
        Get the command item object to access to all the information of the command
        :return: command_descriptor
        """
        command_descriptor: CommandDescriptor
        command_descriptor, module, class_name = self.__command_found
        return command_descriptor

    @property
    def is_manual(self):
        return self.__is_manual

    def run_command(self, bot):
        """
        Execute the command
        :param bot: the bot var, that will be passed to the command. Used to send message and perform actions.
        If you have multiple params to pass to the command use a tuple inside the bot or a dict
        """
        if self.is_manual:
            self.__is_manual = False
            return

        command_descriptor, module, class_name = self.__command_found

        command_class = getattr(module, class_name)

        try:
            command = command_class(bot, self.language, command_descriptor, self.arg, self.params)
            command.run()
        except Exception as exc:
            self.error = 'Error during command execution'
            raise exc

    def run_manual(self, max_chunk_len=1500):
        """
        :param max_chunk_len: the max len of the text
        :return: an array of strings, where each string has the max len of the max_chunk_len
        """
        self.error = 'Error during manual execution'

        commands_descriptor = []
        for cd in self.__command_list:
            commands_descriptor.append(cd[0])

        manual = Manual(self.language, commands_descriptor, self.arg, self.params)
        m = manual.run()

        if len(m) <= max_chunk_len:
            out = [m]
        else:
            out = []
        """
        Cut the manual in chunks and return the chunks array
        This is made because some chats have a limit in message len
        """
        while len(m) > max_chunk_len:
            chunk = m[:max_chunk_len]
            m = m[max_chunk_len:]
            out.append(chunk)

        return out

    def __read_command_structure(self, text):
        """
        :param text: must be a string
        :return: argument as string, parameters as tuple [parameter, data]

        example:
        mal the cat is on the table -f lol this is cute -d 12
        """
        text_list = text.split()

        self.trigger = text_list.pop(0)  # remove the command trigger

        if len(text_list) is 1:
            self.arg = text_list[0]

        read_params = False
        current_param = None
        while text_list:
            word = text_list.pop(0)

            if str.startswith(word, '-'):
                read_params = True
                current_param = text_list[1:]
                self.params[current_param] = None

            elif read_params:
                self.params[current_param] += word + ' '

            else:
                self.arg += word + ' '
