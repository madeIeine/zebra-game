import random
print("""Welcome to Zebra! You stole a zebra from the Bronx Zoo, and now the cops are chasing
      you across New York city!""")

done = False
miles = 20
thirst = 0
tired = 0
enemyMiles = 0
bottle = 3


while not done:
    print("""A. Drink water
B. Run at moderate speed with your zebra.
C. Run at full speed.
D. Stop and take a nap
E. Status check.
Q. Quit""")
    ui = input("The choice is yours: ").upper()
    if(ui == "Q"):
        done = True
        print( "Thanks for playing")
    elif ui == "E":
        print("Miles Traveled:", miles)
        print("You are", thirst, "level of thirst")
        print("Your zebra is", tired, "level of tired")
        print("Drinks left: ", bottle)
        print("The cops are",(miles -enemyMiles), "miles behind")
    elif ui == "D":
        tired = 0
        bottle = 3
        print("Your zebra is refreshed and you refill your water bottle")
        enemyMiles += random.randrange(7, 15)
    elif ui == "C":
        FastSpeed = random.randrange(10, 20)
        miles += FastSpeed
        print("You have traveled",FastSpeed, "miles" ) 
        thirst += 1
        tired += 3
        enemyMiles += random.randrange(7, 15)
    elif ui == "B":
        moderateSpeed = random.randrange(8, 18)
        miles += moderateSpeed
        print("You have traveled",moderateSpeed, "miles")
        thirst += 1
        tired += 1
        enemyMiles += random.randrange(7, 16)
    elif ui == "A":
        if bottle >0:
            bottle-=1
            thirst=0
            print("You drank water and quench your thirst")
            print("You have",bottle,"drinks left")
        else:
            print("You have no water left")
            
        enemyMiles += random.randrange(7, 16)
    if (enemyMiles >= miles):
        print("The cops have caught you.Game over.")
        done = True
    elif (miles-enemyMiles)<8:
        print("Your enemy is close.")
        
    if tired >8:
        print("Your zebra died of tiredness.")
        done = True
    elif tired>6:
        print("You are very tired.")


    if thirst >8:
        print("You died of thirst.")
        done = True
    elif thirst >7:
        print("You are almost dead from thirst.")
    



    if miles>200:
        print("You won!")
        done = True
