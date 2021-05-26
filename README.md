# concord (really WIP)
Discord client made in Qt5

Also uses its own custom api based on QtNetwork and QtWebSockets for contacting the discord servers

## Develop:

To run the example files, make sure that the file `token.txt` exists at `concord/token.txt` containing the user token for the account on which to test things

You can also create this file by running `python3 -m concord.login` and login using the command line, however capcha solving is not implemented so it might not always work (you can always place a token in `concord/token.txt` manually too)
