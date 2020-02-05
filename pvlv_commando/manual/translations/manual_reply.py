from pvlv_commando.languages.languages_handler import language_selector


def invocation(language, invocation_word):

    invocations = ', '.join(invocation_word)

    def eng(): return '**Alternative Invocations:**\n**{}**'.format(invocations)
    def ita(): return '**Invocazioni Alternative:**\n**{}**'.format(invocations)

    return language_selector(
        language,
        eng, ita=ita
    )


def beta(language):

    def eng(): return '**This is a BETA command**\nExpect some errors or malfunctions from this command.'
    def ita(): return '**Questo è un comando in BETA**\nAspettati alcuni errori o malfunzionamenti.'

    return language_selector(
        language,
        eng, ita=ita
    )


def handled_args(language):

    def eng(): return 'Handled Arguments:'
    def ita(): return 'Argomenti Gestiti:'

    return language_selector(
        language,
        eng, ita=ita
    )


def handled_params(language):

    def eng(): return 'Handled Parameters:'
    def ita(): return 'Parametri Gestiti:'

    return language_selector(
        language,
        eng, ita=ita
    )


def command_mask(language, prefix, main_command, sub_call):

    main_command = main_command.replace('_', '.')

    def eng():
        out = '**Shortcut command**\nObtained from command {}{}\nIn substitution of **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    def ita():
        out = '**Comando abbreviato**\nOttenuto dal comando {}{}\nIn sostituzione a **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    return language_selector(
        language,
        eng, ita=ita
    )
