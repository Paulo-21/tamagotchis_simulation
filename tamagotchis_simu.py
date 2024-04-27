import time

tama = """
 _                                    _       _     _    .^._.^.
| |                                  | |     | |   (_)   | 0 0 |
| |_ __ _ _ __ ___   __ _  __ _  ___ | |_ ___| |__  _   ( \---/ )
| __/ _` | '_ ` _ \ / _` |/ _` |/ _ \| __/ __| '_ \| |  .'     '.
| || (_| | | | | | | (_| | (_| | (_) | || (__| | | | |  |/     \|
 \__\__,_|_| |_| |_|\__,_|\__, |\___/ \__\___|_| |_|_|   \ /-\ /
                           __/ |                          V   V
                          |___/                       """
print(tama)
all_tamag = []
croquette_dispo = 50
fight_club = { "state": False, "last_time_check" : 0}
for i in range(5):
    dico_tama = {"faim" : 200, "santé" : 200, "ennui" :200}
    all_tamag.append(dico_tama)

def is_lost():
    for tama in all_tamag:
        if tama["faim"] <= 0 or tama["santé"] <= 0:
            return True
    return False
def print_state():
    print("TIME DAY : ", int(time.perf_counter()-day_start) , " / ", 3*60, " sec")
    print("CROQUETTE : ", croquette_dispo)
    for index, tama in enumerate(all_tamag):
        print("Tamagotchi n°", index+1, " : Santé : ", tama["santé"], ", Faim : ",tama["faim"] ," Ennui : ", tama["ennui"] )
def jouer_avec(n):
    all_tamag[n]["ennui"] += 50

def manger_avec(n):
    global croquette_dispo
    if croquette_dispo  > 0:
        all_tamag[n]["faim"] += 50
        croquette_dispo = croquette_dispo -1
day_start = time.perf_counter()
tic = time.perf_counter()
while True:
    #1.
    print_state()
    s = input("Command : ").split()
    print("---------------------------------------------")
    if len(s) == 2:
        cmd = s[0]
        n = int(s[1])-1
        if n < 0 or n > 4 :
            cmd = None
            print("Tamagotchis n° entre 1 et 5")
        else :
            cmd = cmd.lower()
        #2.
        if cmd == "manger" or cmd == "m":
            manger_avec(n)
        elif cmd == "jouer" or cmd == "j":
            jouer_avec(n)
    if int(time.perf_counter()-tic) < 1:
        continue
    tac = time.perf_counter()
    
    #3.
    time_elapsed_from_last_cmd = int(tac-tic)
    loos_faim = time_elapsed_from_last_cmd * 5
    loos_ennui = time_elapsed_from_last_cmd * 3
    wanna_fight_bro = False
    for tama in all_tamag:
        tama["faim"] -= loos_faim
        tama["ennui"] -= loos_ennui
        if tama["ennui"] <= 0:
            tama["ennui"] = 0
        if tama["ennui"] <= 0:
            wanna_fight_bro = True
            if fight_club["state"] == False:
                fight_club["state"] = True
                fight_club["last_time_check"] = time.perf_counter()
    
    if fight_club["state"] == True:
        time_in_fight = int(time.perf_counter() - fight_club["last_time_check"])
        for tama in all_tamag:
            tama["santé"] -= time_in_fight * 5
        fight_club["last_time_check"] = time.perf_counter()
    if wanna_fight_bro == False:
        fight_club["state"] = False
    if int(time.perf_counter()-day_start) >= 60 * 3:
        for tama in all_tamag:
            tama["santé"] += 50
            tama["ennui"] += 50
            croquette_dispo += 50
            day_start = time.perf_counter()
    #4.
    if is_lost():
        print("YOU LOST")
        break
    tic = time.perf_counter()
    
    