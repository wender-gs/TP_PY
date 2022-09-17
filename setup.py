import os

directory_app = r".\TP_PY"
directory_db = r".\db"


if not os.path.exists(directory_db):
    print("criando diretorio db")
    os.system("mkdir db")
    os.system("cd db && call >> dados.txt")


def executeapp():
    os.system("cd TP_PY && python app.py")


if os.path.exists(directory_app):
    executeapp()
else:
    os.system("git clone https://github.com/wender-gs/TP_PY.git")
    executeapp()
