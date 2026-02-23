** start of main.py **

full_dot = '●'
empty_dot = '○'
def create_character(name,strength, intelligence, charisma):
    #Conditions for checking name
    if not type(name) == str:
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name)>10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    #Conditions for checking legitimacy of the stat variables
    if not all(isinstance(stat, int) for stat in (charisma, intelligence, strength)):
        return "All stats should be integers"
    if any(var < 1 for var in(strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    if any(var > 4 for var in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    if strength+intelligence+charisma != 7:
        return "The character should start with 7 points"
    
    empty_strength = 10 - strength
    empty_intelligence = 10 - intelligence
    empty_charisma = 10 - charisma 
    return f"{name}\nSTR {full_dot*strength+empty_strength*empty_dot}\nINT {full_dot*intelligence+empty_intelligence*empty_dot}\nCHA {full_dot*charisma+empty_charisma*empty_dot}"

        
        



** end of main.py **

