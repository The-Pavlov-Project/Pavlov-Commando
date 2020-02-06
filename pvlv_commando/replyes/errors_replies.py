from pvlv_commando.languages.languages_handler import language_selector


def guild_not_pro(language):

    def eng(): return 'This guild has not the right pro status to run this command.'
    def ita(): return 'Questa gilda non ha un pro status sufficiente per eseguire quest comando.'

    return language_selector(
        language,
        eng, ita=ita
    )


def command_not_found(language):

    def eng(): return 'This is not a command.'
    def ita(): return 'Questo non è un comando.'

    return language_selector(
        language,
        eng, ita=ita
    )


def manual_execution_fail(language):

    def eng(): return 'There is a problem in the manual of this command.'
    def ita(): return 'C\'è un problema nel manuale di questo comando.'

    return language_selector(
        language,
        eng, ita=ita
    )


def command_execution_fail(language):

    def eng(): return 'Error during command execution.'
    def ita(): return 'Errore durante l\'esecuzione del comando.'

    return language_selector(
        language,
        eng, ita=ita
    )


def parse_error(language, argument, suggestion):

    def eng(): return 'The value: "{}" is not valid.\nTry something like "{}".'.format(argument, suggestion)
    def ita(): return 'Il valore: "{}" non è valido.\nProva ad usare "{}".'.format(argument, suggestion)

    return language_selector(
        language,
        eng, ita=ita
    )


def arg_not_found_error(language):

    def eng(): return 'The argument of this command is wrong or not existent.'
    def ita(): return 'L\'argomento di questo comando è errato o inesistente.'

    return language_selector(
        language,
        eng, ita=ita
    )


def arg_void_not_allowed(language):

    def eng(): return 'You cant leave the argument void in this command.'
    def ita(): return 'L\'argomento in questo comando non può essere vuoto.'

    return language_selector(
        language,
        eng, ita=ita
    )
