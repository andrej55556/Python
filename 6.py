import  random
states = ["в спальне","на кухне","в ванной","в коридоре"]
where = ["в спальню","на кухню","в ванную","в коридор","в окно","в дверь"]

def f(state):
    print("# Вы {}. Куда идём?".format(states[state-1]))    
    match state:
            case 1:
                print("# 1 - {}".format(where[2]))
                print("# 2 - {}".format(where[3]))
                state = int(input())
                match state:
                     case 1:
                          f(3)
                     case 2:
                          f(4)
            case 2:
                print("# 1 - {}".format(where[4]))
                print("# 2 - {}".format(where[3]))
                state = int(input())
                match state:
                     case 1:
                          return print("Вы разбились и проиграли!")
                     case 2:
                          f(4)
            case 3:
                print("# 1 - {}".format(where[0]))
                print("# 2 - {}".format(where[3]))
                state = int(input())
                match state:
                     case 1:
                          f(1)
                     case 2:
                          f(4)
            case 4:
                print("# 1 - {}".format(where[0]))
                print("# 2 - {}".format(where[1]))
                print("# 3 - {}".format(where[2]))
                print("# 4 - {}".format(where[5]))
                state = int(input())
                match state:
                     case 4:
                          return print("Вы покинули дом и выиграли!")
                     case 1:
                          f(1)
                     case 2:
                          f(2)
                     case 3:
                          f(3)
                
f(random.randint(1,4))