# Py-Photos-Organizer

This is a simple script that i made to rename and organize by years and month all my photos in my archive.
## Renamer
The renamer part is took by [rizebi](https://github.com/rizebi/randomScriptsAndProjects) but modified by me to make it runnable in linux. 
It renames photos and videos filenames to a standard timestamp, used by the following script part.
## Organizer
The organizer part and the rest of the code are made entirely by me.
It read filenames to make subfolders ordered by year and month, where the photos will be stored in.
## How to use
It's very easy, but i'll write the needed commands.
Be sure that you have git installed in your system.

    git clone https://github.com/replydev/Py-Photos-Organizer.git
    cd Py-Photos-Organizer
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python main.py
## Contribution
If you wanna contribute, you are welcome!
Just fork it and make a pull request, i will be happy to merge if your changes meet my (low) code standards.