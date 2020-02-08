# fortool-custom-matchmaking-bot
Bot Discord fait en Python permettant de créer des parties personnalisées Fortnite de manière automatique à l'aide de macros lancées depuis un PC dans le Cloud (Windows).</br>
Chaque macro correspond à un mode de jeu, celles-ci peuvent être refaites depuis le logiciel [Macro Recorder](https://www.jitbit.com/macro-recorder/) en faisant attention à garder les mêmes noms de fichiers et extension (.exe).
# Programmes à installer
###### Macro recorder
[Installer Macro Recorder](https://www.jitbit.com/macro-recorder/)
###### Python
[Installer Python](https://www.python.org/downloads/)
# Lancer le bot
1. Changer le token du bot depuis le fichier main.py situé en bas de la page
```
bot.run('TOKEN DE VOTRE BOT', bot=True, reconnect=True)
```
2. Lancer le bot en utilisant le shell de Python depuis le repertoire du bot
```
python main.py
```