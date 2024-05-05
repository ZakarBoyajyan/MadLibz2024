import random

def first_temp():
    input1 = input("Type a number:")
    input2 = input("Measure of time:")
    input3 = input("Mode of transportation:")
    input4 = input("Input an adjective:")
    input5 = input("Input an adjective again:")
    input6 = input("Input a noun:")
    input7 = input("Input a color:")
    input8 = input("Part of the body:")
    input9 = input("Input a verb:")
    input10 = input("Input another number:")
    input11 = input("Input a noun again:")
    input12 = input("Input a noun once more:")
    input13 = input("Part of the body:")
    input14 = input("Input a verb again:")
    input15 = input("Input one more noun:")
    input16 = input("Input the third adjective:")
    input17 = input("Enter a silly word:")
    input18 = input("Input the last noun:")

    print(f"""It was about {input1} {input2} ago when I arrived at the hospital in a {input3}.
        The hospital is a/an {input4} place, there are a lot of {input5} {input6} here.
        There are nurses here who have {input7} {input8}.
        If someone wants to come into my room I told them that they have to {input9} first.
        I’ve decorated my room with {input10} {input11}. Today I talked to a doctor and they were wearing a {input12} on their {input13}.
        I heard that all doctors {input14} {input15} every day for breakfast. The most {input16} thing about being in the hospital is the {input17} {input18}!""")

def second_temp():
    input1 = input("Input a proper noun(Person's name):")
    input2 = input("Input a noun:")
    input3 = input("Input an adjective(Feeling):")
    input4 = input("Input a verb")
    input5 = input("Input an adjective again(Feeling):")
    input6 = input("Input a type of animal:")
    input7 = input("Input a verb again:")
    input8 = input("Input a color:")
    input9 = input("Input a verb(ending in ing):")
    input10 = input("Input an adverb(ending in ly):")
    input11 = input("Type a number:")
    input12 = input("Measure of time:")
    input13 = input("Input another color:")
    input14 = input("Input a type of animal again:")
    input15 = input("Type a number once again:")
    input16 = input("Enter a silly word:")
    input17 = input("Enter a noun last time:")

    print(f"""
        This weekend I am going camping with {input1}.
        I packed my lantern, sleeping bag, and {input2}. I am so {input3} to {input4} in a tent.
        I am {input5} we might see a(n) {input6}, I hear they’re kind of dangerous.
        While we’re camping, we are going to hike, fish, and {input7}.
        I have heard that the {input8} lake is great for {input9}.
        Then we will {input10} hike through the forest for {input11} {input12}.
        If I see a {input13} {input14} while hiking, I am going to bring it home as a pet!
        At night we will tell {input15} {input16} stories and roast {input17} around the campfire!!
    """)


def third_temp():
    input1 = input("input a  proper noun(Person's name):")
    input2 = input("Input an adjective:")
    input3 = input("input a color:")
    input4 = input("Input a type of animal:")
    input5 = input("Input a place:")
    input6 = input("Input an adjective again:")
    input7 = input("Magical Creature(Plural):")
    input8 = input("Input the third adjective:")
    input9 = input("Magical creatue(Plural):")
    input10 = input("Input a room in a house:")
    input11 = input("Input another noun:")
    input12 = input("Input a noun one more time:")
    input13 = input("Input a noun in a plural form:")
    input14 = input("Enter the fourth adjective:")
    input15 = input("Input another noun(Plural):")
    input16 = input("Type a number:")
    input17 = input("Measure of time:")
    input18 = input("Enter a verb(ending in ing):")
    input19 = input("Type the last adjective:")
    input20 = input("And finally, enter a noun:")
 
    print(f"""
        Dear {input1}, I am writing to you from a {input2} castle in an enchanted forest.
        I found myself here one day after going for a ride on a {input3} {input4} in {input5}.
        There are {input6} {input7} and {input8} {input9} here!
        In the {input10} there is a pool full of {input11}.
        I fall asleep each night on a {input12} of {input13} and dream of {input14} {input15}.
        It feels as though I have lived here for {input16} {input17}.
        I hope one day you can visit, although the only way to get here now is {input18} on a {input19} {input20}!!
    """)

keep_asking = True
while keep_asking:
    temp_input = input("Choose one out of the three templates(Type Y for random choice):")

    if temp_input == '1':
        print("You have chosen the first template. You gotta gimmie answers now.")
        first_temp()
        keep_asking = False
    elif temp_input == '2':
        print("You have chosen the second template. Waiting for your answers.")
        second_temp()
        keep_asking = False
    elif temp_input == '3':
        print("You have chosen the third template. I would like to see your answers.")
        third_temp()
        keep_asking = False
    elif temp_input.lower() == 'y':
        choose_rand = random.randint(1,3)
        if choose_rand == 1:
            print("I've chosen the first template for you. Just give me answers.")
            first_temp()
            keep_asking = False
        elif choose_rand == 2:
            print("I've chosen the third template for you. Just give me answers.")
            third_temp()
            keep_asking = False