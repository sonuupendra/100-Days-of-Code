print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("In which direction do you wanna go? Press R for right and L left?\n")

if direction.lower() == "l":
    weapon = input("Please select one: SWORD or RIFLE.\n")
    if weapon.lower() == "sword":
        print('''
              
                          ()
                        __)(__
                        '-<>-'
                          )(   
                          || 
                          || 
                          || 
                          || 
                          || 
                          ||  
                          ||
                          ||  
                          \/ 
              ''')
        print("You may use the weapon for rest of your mission. To proceed, please select a location\n")
        location = input("Choose a location: Forest or Ocean?\n")
        if location.lower() == "forest":
            print("You wandered too far in search of treasure… and got lost.")  
        elif location.lower() == "ocean":
            print("Against the waves, you survived and won the treasure!")
        else:
            print("Provide a correct selection.")
        
    elif weapon.lower()== "rifle":
        print('''
                                            
                     ,1             ,-===========.
                    /,| ___________((____________\\_                _
 ,========.________//_|/===========._#############L_Y_....-----====//
(#######(==========\################\=======.______ --############((
 `=======`"        ` ===============|::::.___|[ ))[JW]#############\\
                                    |####|     ""\###|   :##########\\
                                   /####/         \##\     ```"""=,,,))
                                  /####/           \##\
                                 '===='             `=`
              ''')
        print("You may use the weapon for rest of your mission. To proceed, please select a location\n")
        location = input("Choose a location: Desert or Arctic Ice?\n")
        if location.lower() == "desert":
            print("The scorching desert drained your strength. You got lost in the endless sands.")  
        elif location.lower() == "arctic ice":
            print("You crossed the frozen arctic ice and discovered the hidden treasure. You win!")
        else:
            print("Provide a correct selection.")
    
    else:
        print("Provide a correct selection.")

if direction.lower() == "r":
    weapon = input("Please select one: AXE or CROSSBOW.\n")
    if weapon.lower() == "axe":
        print('''
                
           __
        ,. |_'.
       / / /:\ \
     _/_/_/::: |
    /o_'/o>::/ /
    / /'/:::/ /
   / /_/::.'_/     mrf
  / / \__.-'
 / /
/ /
 /
              
                    
              ''')
        print("You may use the weapon for rest of your mission. To proceed, please select a location\n")
        location = input("Choose a location: Grassland or Antartic Ice?\n")
        if location.lower() == "grassland":
            print("The peaceful grasslands guided you safely to the hidden treasure. You win!")  
        elif location.lower() == "antartic ice":
            print("You wandered across the Antarctic ice and vanished into the endless snow.")
        else:
            print("Provide a correct selection.")
        
    elif weapon.lower()== "crossbow":
        print('''
                .-.                                   
               /  \\                                
          .---/-+--||                               
          |  K=====++->                             
          '---\-+--||                               
               \  //                                 
                `-'      
                                    
              ''')
        print("You may use the weapon for rest of your mission. To proceed, please select a location\n")
        location = input("Choose a location: Ancient Building or Cave?\n")
        if location.lower() == "ancient building":
            print("You entered the ancient building and became trapped in its endless ruins.")  
        elif location.lower() == "cave":
            print("The dark cave led you straight to the legendary treasure. Victory is yours!")
        else:
            print("Provide a correct selection.")
    
    else:
        print("Provide a correct selection.")