# Pavlov Commando

Commands framework to handle text commands in a easy way.

####Example
```python
from pvlv_commando.pvlv_commando import Commando
from pvlv_commando import (
    CommandNotFound,
    CommandExecutionFail,
    ArgVoidNotAllowed,
    ParamNotFound,
    MaxHourlyUses,
    MaxDailyUses,
)

def command_handler():
    com = Commando()
    
    # An example of incoming text from the chat
    text = '.command this is a nice argument -d a text parameter -f -g' 

    """
    permission level of the user in the chat, 
    it will be compared with the permissions needed to run the command,
    specified in the declaration file
    """
    permissions = 10  

    if text.startswith('.'):

        try:
            # text without the command invocation word, and the language of the command
            com.find_command(text[1:], 'eng', permissions)
            
            """
            Optional!
            You can specify in the command declaration file a max time use of the command
            cause of computational weight of the command.
            Build a db where you save the number of executions by the user
            """
            com.hourly_executions = 12
            com.daily_executions = 39

            """
            to run the command you have to pass the bot object,
            that will be used inside commands.
            max_chunk_len: specify the max len of the out, some chats have a limit in length
            """ 
            out = com.run_command(None, max_chunk_len=1500)  
            if out:
                """
                Send to the chat with parse mode enabled 
                ** mean bold
                - if your chat dont support parse mode use com.run_manual().replace('**', '')
                - if your chat have a different parse mode use com.run_manual().replace('**', 'your_format')
                """
                print(out)

        # DO NOT EXPOSE FULL EXCEPTIONS IN CHAT, ONLY THIS ARE READY FOR CHAT

        except CommandNotFound as exc:
            print(exc)

        except ArgVoidNotAllowed as exc:
            print(exc)

        except ParamNotFound as exc:
            print(exc)

        except MaxHourlyUses as exc:
            print(exc)

        except MaxDailyUses as exc:
            print(exc)
        
        except CommandExecutionFail as exc:
            print(exc)  # the exception to send in chat

            # the full report of the exception to send to a log chat or for internal log.
            print(exc.error_report)  
```

##Configurations file of the package:
Must be put in a folder "configs" in the root of the project

configs/commando.cfg

```buildoutcfg
[commands]
COMMANDS_DIR = commands/

[debug]
DEBUG = True
```

## Auto Command creation
With this tool you can automatically create a new command, with the default folders and files
```python
from pvlv_commando import StartCommand


def main():
    # define the module name and the command name (use underscores only)
    nc = StartCommand('new_module', 'new_command')
    nc.create()
    """
    The full command_declaration json file will be created
    Check the command_declaration json file to learn how to set up it
    """

if __name__ == '__main__':
    main()
```
###Command Declaration File
It's a json file called with the same name as the command.py file and the command folder.

**Everything with "OPTIONAL" label in the side comment can be omitted**
#### Example:
```
{
    "management_command": 0,  # OPTIONAL, the commad is owner only
    "beta_command": false,  # OPTIONAL, the command in still in development
    "pro_command": 0,  # OPTIONAL, the command can be run only by pro users (pro level il arbitrary int)
    "dm_enabled": true,  # OPTIONAL, enabled in direct char, 1 to 1 with the bot
    "enabled_by_default": true,  # OPTIONAL, the command must be activare manually by the user
    "permissions": 0,  # OPTIONAL, the permission level to run the command
    "cost": 20,  # OPTIONAL, cost of the command, user might a value to run this command
    "hourly_max_uses": 10,  # OPTIONAL, man uses per hour by user
    "daily_max_uses": 90,  # OPTIONAL, man uses per day by user
    "invocation_words": ["command", "com"],  # the command invocation words
    "description": {
        "eng": "Short description of the command",
        "ita": "Breve descrizione del comando"
    },
    "handled_args": {  # must always contain at least one element, "" rappresent the void one
        "": {
            "eng": "Description of command without args",
            "ita": "Descrizione del comando senza argomenti"
        },
        "arg": {
            "eng": "Description of executions with this argument",
            "ita": "Descrizione dell' esecuzione con questo argomento"
        }
    },
    "handled_params": {  # OPTIONAL, the parameters
        "-param1": {
            "eng": "Description of executions with this parameter",
            "ita": "Descrizione dell'esecizione con questo parametro"
        },
        "-param2": {
            "eng": "Description of executions with this parameter",
            "ita": "Descrizione dell'esecizione con questo parametro"
        }
    }
}
```
### Command Class Example
This is the command file that will be run when the command is invoked
```python
class CommandName(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot  # bot entity to send messages, the one that you pass on run command
        self.language = language  # the language detected in the guild, to personalize responses
        self.command = command  # the command descriptor of the command

        self.arg = arg  # the detected arg

        """
        parameters will be initialized here
        You have to reserve the vars here that you need to use
        in _vars must be the same name as handled_params in the config json but without dash (-) 
        """
        self._param1 = None  # the detected parameters
        self._param2 = None

        for param in params:  # read the parameter from the params dict and save them in vars over here
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def run(self):
        print('Command has been run arg: {}'.format(self.arg))
```

