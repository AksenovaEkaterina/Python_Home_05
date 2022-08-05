# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется 
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Игрок против игрока
def Candy (N):
    import random
    listPlayer = [1, 2]
    Player = int(random.choice(listPlayer))
    while N>0:
        if (N>27):
            print ("Игрок ", Player, ", берите конфеты ")    
            CountCandy = int(input("Введите количество конфет от 1 до 28---> "))
            if CountCandy not in range (1,29): CountCandy = int(input("Количество конфет должно быть от 1 до 28--->   "))
        if (N<28) and (N>0):
            print ("Игрок," , Player, "берите конфеты ")
            print ("Введите количество конфет от 1 до ", N)
            CountCandy = int(input("---> "))

        N=N-CountCandy
        if N==0 or N<0: break
        else: 
            print ('Остатось', N, 'конфет')
            if Player==1:  Player=2
            else: Player =1 
    print ("Конец игры. Победил игрок ", Player)    
Candy (50)



# Игорок против бота
# def Candy (N):
#     import random
#     listPlayer = [1, 2]
#     Player = random.choice(listPlayer)
#     while N>0:
#         if (N>27):
#             if Player==1:
#                 print ("Игрок, берите конфеты ")
#                 CountCandy = int(input("Введите количество конфет от 1 до 28---> "))
#                 if CountCandy not in range (1,29): CountCandy = int(input("Количество конфет должно быть от 1 до 28.  --->   "))
#             else:
#                 print ("Бот берет конфеты ")
#                 CountCandy = random.randint(1,28)
#                 print ("Бот взял -->", CountCandy, "конфет" )
        
#         if (N<28) and (N>0):
#             if Player==1: 
#                 print ("Игрок, берите конфеты ")
#                 print ("Введите количество конфет от 1 до ", N)
#                 CountCandy = int(input("---> "))
#                 if CountCandy not in range (1,N+1): 
#                     print ("Количество конфет должно быть от 1 до ", N)
#                     CountCandy = int(input("---> "))
#             else:
#                 CountCandy = random.randint(1,N)
#                 print ("Бот взял -->", CountCandy, "конфет" )
        
#         N=N-CountCandy
    
#         if N==0 or N<0: break
#         else: 
#             print ('Остатось', N, 'конфет')
#             if Player==1:  Player=2
#             else: Player =1 
#     if Player ==1: print ("Конец игры. Победил Игрок") 
#     else: print ("Конец игры. Победил Бот") 
# Candy (50)
       
    
   

