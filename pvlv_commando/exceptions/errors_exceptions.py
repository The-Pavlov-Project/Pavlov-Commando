from pvlv_commando.replyes.errors_replies import (
    command_not_found,
    manual_execution_fail,
    command_execution_fail,
)
from pvlv_commando.exceptions.command_error_report import command_error_report


class CommandException(Exception):
    def __init__(self, language, full_exception=None, command=None, arg=None, params=None):
        """
        :param language: the language
        :param command: the self of commando
        :param arg: the exception catch if existed
        :param params: the exception catch if existed
        """
        self.language = language
        self.full_exception = full_exception
        self.command = command
        self.arg = arg
        self.params = params
        self.error_report = None


class CommandNotFound(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = command_not_found(self.language)

    def __str__(self):
        return self.public_exc


class CommandExecutionFail(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = command_execution_fail(self.language)
        self.error_report = command_error_report(
            self.public_exc,
            self.full_exception,
            self.command,
            self.arg,
            self.params,
        )

    def __str__(self):
        return self.public_exc


class ManualExecutionFail(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = manual_execution_fail(self.language)
        self.error_report = command_error_report(
            self.public_exc,
            self.full_exception,
            self.command,
            self.arg,
            self.params,
        )

    def __str__(self):
        return self.public_exc

