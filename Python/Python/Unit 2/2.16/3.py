print("You have to escape the island you are stuck on, but be careful there are wild beasts roaming on this island")

jun_1 = input("While your escaping you come across 2 paths one towards the left and one towards the right, the left one feels more ominous")

if jun_1.lower() == "left":
 print("As you walk you start to feel weak and then you realize you are bleeding but its too late you pass out from blood lost")
elif jun_1.lower() == "right":
    print("You feel like you made the right choice")

jun_2 = input("After a while of walking it starts raining you can either hide in a cave near by or hide in the trees")

if jun_2.lower() == "cave":
    print("In the cave you get attacked by a bear also hiding from the rain")
elif jun_2.lower() == "trees":
    print("Once the rain dies down you notice a bear coming out of the cave")

jun_3 = input(
"You find a beach, you look around you see some rope and wood, you come up with 2 options either build a raft out of the wood and rope or start a fire and hope someone sees it"
)

if jun_3 == "fire":
    print("You decided to build a fire, after what feels like forever you seem a bout in the distance help has arrived and you can finally leave the island")

elif jun_3 == "raft":
    print("You decided to make a raft, you build the raft and set sail but than you see some 3 fins in the water, there sharks you end up packing and falling into the water")