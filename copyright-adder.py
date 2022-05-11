import os

path = "/path/to/files/"
extensions = ["cpp", "h"]
copyright = ["/**********************************************\n",\
             "* Invented License 2022 \n"
             "**********************************************/\n\n"]
ignore = ["dir_to_ignore1", "dir_to_ignore2"]

def add_copyright(directory):
    f = open(directory, 'r')
    lines = f.readlines()
    print("Adding copyright to file: " + directory)
    if lines[0] != copyright[0]:
        f = open(directory, 'w')
        f.writelines(copyright)
        f.writelines(lines)

def explore(path):
    for filename in os.listdir(path):
        if filename not in ignore:
            directory = os.path.join(path, filename)
            if os.path.isdir(directory):
                explore(directory)
            elif os.path.isfile(directory):
                ext = directory.split(".")[-1]
                if ext in extensions:
                    add_copyright(directory)

explore(path)
