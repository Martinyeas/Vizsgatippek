import os

kiiratas = open(f"{os.path.dirname(__file__)}/fajlnevek.txt","w", encoding="utf-8")
fajlok = os.listdir(os.path.dirname(__file__))


for i in fajlok:
    if ".pdf" in i:
        struktura = f'<li><button onclick="opn(\'{i}\')">{i[0:-4]}</button></li>'
        kiiratas.write(struktura + "\n")

kiiratas.close()