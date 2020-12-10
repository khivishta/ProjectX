/////////////////////////////////////////////////////////////////////////

Installation Guide

1)Unzip all the files into a folder, then open the folder named 'src'.
2)Within this folder open the file 'game.py'.
3)Enjoy the game!





/////////////////////////////////////////////////////////////////////////

If the game show "No response' after one run, don't close it and just want for few seconds， it will work again.


if the error: FileNotFoundError: No such file or directory is produced follow 
these steps below to start the game:
1) copy all the contents of the folders 'img' and 'sound' into the same folder 
as 'src'
2) open all the .py files in the 'src' folder, and remove any code containing 
the code: 'img/' or 'sound/' within these files 

For example:
line 190 in 'game.py' : sound_crash = pygame.mixer.Sound("sound/crash.ogg")
would be modified into:
sound_crash = pygame.mixer.Sound("crash.ogg")

3) run the code and enjoy!


///////////////////////////////////////////////////////////////////////