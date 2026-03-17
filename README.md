Welcome to the Bear Hook Guide.

First of all you need to download the "bearhook.py" to your PC. Contain it in a folder, Open the cmd and type "cd -your_file_location-"
now you granted access from your cmd to the folder.

Open the file with an IDE

Change the webhook variable to your own webhook URL created from discord.
If you want to leave a message follow the instructions there. you can also change the message you wanna put, The text files name.

Dont forget that you can customize this to make it worse for the victims.

After doing all the things, Open the cmd you opened. Dont forget to install PyInstaller before doing this.

Write (DO NOT CHANGE THE FILE NAME):
python -m PyInstaller --onefile --noconsole bearhook.py

after doing it, Go to the created "dist" file and the exe will be ready there. You can change it to make it look less suspicious like "Realtek Audio Service"
IF YOU want a custom icon, Save your icon inside the folder with the name "icon". The extension should be .ico
so it needs to look like this: "icon.ico"

Now you want to run a different code from the first one.
Write:
python -m PyInstaller --onefile --noconsole --icon="icon.ico" bearhook.py

And do the same things.

You can always make this work with different ways since its open source. Most of the time people are going to use this as a Dropper Virus.
But like i said, You can customize it. I have a stronger evolution of this file but i cant post it here.

Feel free to use it. but dont forget that YOU USE THIS AT YOUR OWN RISK. I DONT HAVE ANYTHING TO DO IF YOU FACE ANY CONSUQUENCES.

A Showcase that how it will look:
<img width="1062" height="787" alt="Screenshot 2026-03-15 163549" src="https://github.com/user-attachments/assets/e1049341-6322-48ff-afa6-71aca0c6f067" />
