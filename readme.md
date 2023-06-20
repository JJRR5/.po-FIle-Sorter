# 📝 .po File Sorter 🌐

This is a simple Python 🐍 script that helps you sort the terms in your .po translation files alphabetically. It can be quite handy when you're working on localizing your software.

## 🛠️ How it works

The script scans all .po files in your current working directory. If it finds exactly one file, it sorts it alphabetically.

If it finds more than one .po file, it asks you to enter the name of the file you want to sort. If it doesn't find any .po file, it simply informs you and exits.

The sorting is based on the 'msgid' key of the terms.


## 🔧 Requirements

You need Python 3 and the polib library installed in your environment. You can install polib with pip:

```bash
pip install polib
```

## 🏃‍♂️ How to run the script

You can run the script with the following command:

```bash
python3 script.py
```

🎯 Recommendation
For ease of use, it is recommended to create an alias for the script:

```bash
alias sort_translations="python3 ~/Personal/Scripts/POOSorter/script.py"
```

Add the above line to your shell's configuration file (e.g., .bashrc, .zshrc, etc.) to have the alias available in every new terminal session.

With this alias, you can simply type sort_translations in the terminal to run the script, no matter what your current directory is. Just make sure to replace ~/Personal/Scripts/POOSorter/script.py with the actual path to the script on your machine.

And there you have it! Enjoy your neatly sorted .po files! 🎉📚
