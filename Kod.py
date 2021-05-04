import pyautogui as pg
import hashlib as hl
por = pg.confirm("Vyberte si možnosť", "Databaz v1.0.1", buttons=["Prihlásenie", "Registrácia"])
hashovaneheslo=""
if por == "Registrácia":    
    name = pg.prompt("Aké je tvoje uživateľské meno?", "Meno", "Sem ho napíš")
    hashovanename = hl.sha1(name.encode()).hexdigest()
    heslo = pg.password("Vytvorte si svoje heslo", "Heslo", "", "*")
    hashovaneheslo = hl.sha256(heslo.encode()).hexdigest()
    with open(".ignore","a") as file_:
        file_.write(str(hashovanename))
        file_.write('; ')
        file_.write(str(hashovaneheslo))
        file_.write('\n')
elif por == "Prihlásenie":
    name = pg.prompt("Aké je tvoje uživateľské meno?", "Meno", "Sem ho napíš")
    if name == "Sem ho napíš":
        pg.alert("Zadajte prosím meno.")
    if name == None:
        pg.confirm("Chcete ukončiť program?", "Koniec", buttons=("Áno", "Nie"))
    with open(".ignore","r") as file_:
        f=file_.readlines()
        chcecker=False
        for line in f: 
            docasny_text=""
            docasny_list=[]
            if line[-1] == '\n':
                docasny_text+=(line[:-1])
            else:
                docasny_text+=(line)
            docasny_list=docasny_text.split("; ")
            k=0
            while k<5:
                hashovanename = hl.sha1(name.encode()).hexdigest()
                if docasny_list[0] == hashovanename:
                    chcecker=True
                    heslo = pg.password("Zadajte svoje heslo", "Heslo", "", "*")
                    if heslo == None:
                        break
                    hashovaneheslo = hl.sha256(heslo.encode()).hexdigest()
                    if hashovaneheslo == docasny_list[1]:
                        pg.alert("Bol si úspešne prihlásený.")
                        break
                    else:
                        pg.alert("Zadané heslo je nesprávne. Skús to znova.")
                        k+=1
                else:
                    break
        if chcecker == False:
            pg.alert("Zadané meno nie je v databáze. Registrujte sa.")