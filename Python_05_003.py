# Создайте программу для игры в ""Крестики-нолики"".

def XX_00(N):
    l = [['1','2','3'],['4','5','6'],['7','8','9']]
    for i in l: print (i, '\n')
    PlayerList = [1,2]
    import random
    player=random.choice(PlayerList)
    while (l[0][0] and l[0][1] and l[0][2])!="X" or(l[1][0] and l[1][1] and l[1][2])!="X" or  (l[2][0] and l[2][1] and l[2][2])!="X" or (l[0][0] and l[1][0] and l[2][0])!="X" or(l[0][1] and l[1][1] and l[2][1])!="X" or (l[0][2] and l[1][2] and l[2][2])!="X" or (l[0][0] and l[1][1] and l[2][2])!="X" or(l[0][2] and l[1][1] and l[2][0])!="X":
        while (l[0][0] and l[0][1] and l[0][2])!="0" or(l[1][0] and l[1][1] and l[1][2])!="0" or  (l[2][0] and l[2][1] and l[2][2])!="0" or (l[0][0] and l[1][0] and l[2][0])!="0" or(l[0][1] and l[1][1] and l[2][1])!="0" or  (l[0][2] and l[1][2] and l[2][2])!="0" or (l[0][0] and l[1][1] and l[2][2])!="0" or(l[0][2] and l[1][1] and l[2][0])!="0":
            print("Игрок", player, "выберите номер строки")
            X = int(input ('--> '))
            X-=1
            print("Игрок", player, "выберите номер столбца")
            Y = int(input ('--> '))
            Y-=1
            if player==1:
                l[X][Y]="X"
                player=2
            else: 
                l[X][Y]="0"
                player=1
            for i in l: print (i, '\n')
    print ("Победил игрок", player )

XX_00(1)