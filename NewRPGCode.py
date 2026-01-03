full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'

    stats = [strength, intelligence, charisma]

    for numbers in stats:
        if not isinstance(numbers, int):
            return 'All stats should be integers'
        if numbers < 1:
            return 'All stats should be no less than 1'
        if numbers > 4:
            return 'All stats should be no more than 4'
    
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    strengthFormula = strength * full_dot + empty_dot * (10 - strength)

    intelligenceFormula = intelligence * full_dot + empty_dot * (10 - intelligence)

    charismaFormula = charisma * full_dot + empty_dot * (10 - charisma)

    return f'{name}\nSTR {strengthFormula}\nINT {intelligenceFormula}\nCHA {charismaFormula}'

create_character('ren', 4, 2, 1)
