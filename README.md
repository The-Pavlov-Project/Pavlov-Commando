# Pavlov Commando

To handle commands in a easy way

##Example
```python
from pvlv_commando.pvlv_commando import Commando
from pvlv_commando import CommandExecutionFail, ManualExecutionFail

def handler():
    com = Commando()
    text = '.command la vita se bella -d ciao -f -g'  # An example of incoming text from the chat
    permissions = 10

    if text.startswith('.'):

        try:
            # text without the command invocation word, and the language of the command
            com.find_command(text[1:], 'eng', permissions)

            """
            Send to the chat with parse mode enabled 
            ** mean bold
            - if your chat dont support parse mode use com.run_manual().replace('**', '')
            - if your chat have a different parse mode use com.run_manual().replace('**', 'your_format')
            """
            man = com.run_manual()
            print(man) if man else None

            com.run_command(None)  # here you have to pass the bot object that will be used

        # Do exception handling as you please
        except CommandExecutionFail as exc:
            print(exc)  # the exception to send in chat
            print(exc.error_report)  # the full report of the exception to send to a log chat or for internal log.

        except ManualExecutionFail as exc:
            print(exc)  # the exception to send in chat
            print(exc.error_report)  # the full report of the exception to send to a log chat or for internal log.

        except Exception as exc:
            print(exc)  # the exception to send in chat
```

##Configurations file:
Must be put in a forder "configs" in the root of the project

configs/commando.cfg

```buildoutcfg
[commands]
COMMANDS_DIR = commands/

[debug]
DEBUG = True
```

### Auto Command creation
With this tool you can automatically create a new command, with the default folders and files
```python
from pvlv_commando import NewCommand


def main():
    # define the module name and the command name (use underscores only)
    nc = NewCommand('new_module', 'new_command')
    nc.create()


if __name__ == '__main__':
    main()
```
