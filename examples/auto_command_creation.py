from pvlv_commando import StartCommand


def main():
    nc = StartCommand('new_module', 'new_command')
    nc.create()


if __name__ == '__main__':
    main()
