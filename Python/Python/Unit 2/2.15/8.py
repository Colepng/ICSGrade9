have_pet = input("Do you have a pet ")

if have_pet.lower() == "yes":
    pet_name = input("What is your pet's name? ")
    if pet_name.lower() == "speedy":
        print("I used to have a pet tortoise called Speedy... He ran away!")
    else:
        print("That's a cool name")
else:
    print("It's OK, we can share my pet shark!")