import subprocess


# define the commands you want to execute
def script_to_run():
    # Need to change these commands to input the data into the database
    # Perhaps just get it to open python shell
    # Then physically try add one item recording the successful commands into this
    # Get the name of the Framework passed over to this
    commands = [
        'python manage.py shell',
        'hello_world()'
    ]

    # loop through the commands and execute them
    for command in commands:
        subprocess.run(command, shell=True)


def hello_world():
    print("ChatGPT Advice")
