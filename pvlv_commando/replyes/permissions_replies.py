from pvlv_commando.languages.languages_handler import language_selector


def insufficient_permission(language):

    def eng(): return 'Error during Command execution'
    def ita(): return 'Errore durante l\'esecuzione del comando'

    return language_selector(
        language,
        eng, ita=ita
    )
