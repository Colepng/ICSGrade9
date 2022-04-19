new_high_score = int(input("Please input your score "))
high_score = 101500
if new_high_score > high_score:
    high_score = new_high_score
    print("Congrats you set the new high score")
else:
    print("You did not beat the high score")