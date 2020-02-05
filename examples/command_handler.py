from pvlv_commando.pvlv_commando import Commando


def main():

    com = Commando()
    # text = '.command'  # An example of incoming text from the chat
    text = '.man'

    if text.startswith('.'):
        try:
            # text without the command invocation word, and the language of the command
            com.find_command(text[1:], 'eng')

            if com.is_manual:
                """
                Send to the chat with parse mode enabled 
                ** mean bold
                - if your chat dont support parse mode use com.run_manual().replace('**', '')
                - if your chat have a different parse mode use com.run_manual().replace('**', 'your_format')
                """
                print(com.run_manual())
            else:
                com.run_command(None)  # here you have to pass the bot object that will be used

        except Exception as exc:
            print(exc)  # for internal log

            print(com.error)  # send to chat a message to notify the error


if __name__ == '__main__':
    main()
