full_dot = '●'
empty_dot = '○'

# Create a Character Function with
# the input parameters: name, strength, intelligence, charisma
def create_character(name, strength, intelligence, charisma):

    # if not isinstance(name, str) checks if the input parameter
    # is a string and then returns the message if it isn't.
    if not isinstance(name, str):
        return 'The character name should be a string'

    # if name == "" checks if the "name" input parameter is empty
    # and returns the message if it is
    if name == "":
        return 'The character should have a name'

    # if len(name) > 10: checks if the length of the name is
    # longer than 10 and returns the message if it is
    if len(name) > 10:
        return 'The character name is too long'

    # if " " in name: checks if there is a space in the name
    # and returns the message if there is
    if " " in name:
        return 'The character name should not contain spaces'

    # I have created a variable that has a list of the other
    # input parameters representing the stats
    stats = [strength, intelligence, charisma]

    # for numbers in stats: loops the list
    # "numbers" stands for each input parameter in the list
    # "stats" stands for the variable name of the list
    for numbers in stats:
        # if not isinstance(numbers, int): check if each integer
        # within the list of input parameters are an integer and returns
        # the message if it isn't
        if not isinstance(numbers, int):
            return "All stats should be integers"

    # using the same loop above to loop through the inout parameters in the list
    for numbers in stats:
        # if numbers < 1: checks if each integer within the list of input
        # parameters are smaller/less than 1 and returns the message
        # if it isn't
        if numbers < 1:
            return 'All stats should be no less than 1'

    # using the same loop above to loop through the inout parameters in the list
    for numbers in stats:
        # if numbers > 4: checks if each integer within the list of input
        # parameters are bigger/greater than 4 and returns the message
        # if it isn't
        if numbers > 4:
            return 'All stats should be no more than 4'

    # if strength + intelligence + charisma != 7: checks if the total sum of the
    # input parameters is not 7 and returns the message if it isn't
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    # This variable consists of the formula that displays the amount of full_dots and
    # empty_dot's according to the input parameters.
    # strength * full_dot - since full_dot is one string,
    # for example, it is the same as 4 x 1 if strength was 4
    # empty_dot * (10 - strength) - the number 10 is there because
    # thats the amount of dots that should be displayed in total.
    # the subtraction within the parenthesis takes place
    # first, for example, 10 - 4 if strength was 4, with the answer being 6.
    # Then the multiplication formula empty_dot * 6 is the same as the full_dot multiplication
    # which finds out how many empty_dots are left, meaning that empty_dot * 6
    # is the same as 1 x 6. Adding them both together leaves with
    # 4 full_dots and 6 empty_dots.
    # This formula is then repeated for intelligence and charisma
    formulaStrength = strength * full_dot + empty_dot * (10 - strength)

    formulaIntelligence = intelligence * full_dot + empty_dot * (10 - intelligence)

    formulaCharisma = charisma * full_dot + empty_dot * (10 - charisma)

    # (WRONG CODE) I only kept this code in as it was my first code.
    # The reason why it doesn't work is because returning a variable with a print function
    # will return None instead of the formatted stat.
    # fullstat = print(f'{name}\nSTR {formulaStrength}\nINT {formulaIntelligence}\nCHA {formulaCharisma}')

    # I used an if True loop to display the stat.
    if True:
        # This returns the stat using f-strings and new lines (\n)
        return f'{name}\nSTR {formulaStrength}\nINT {formulaIntelligence}\nCHA {formulaCharisma}'

# Print is then used to call the function with the arguements and display the returned value
print(create_character('ren', 4, 2, 1))
