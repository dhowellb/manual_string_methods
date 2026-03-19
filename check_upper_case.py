# Function na sariling gawa para i-recreate ang .isupper() method
def check_upper_case(target_string):
    # Reference list para sa malalaki at maliliit na letra
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Tracker kung may nahanap tayong kahit isang malaking letra (default ay False)
    has_upper_letter = False
    
    # Isa-isang i-check ang bawat character sa string
    for character in target_string:
        # Kung may nakitang maliit na letra, ibig sabihin hindi lahat uppercase. I-return agad ang False!
        if character in lower_letters:
            return False
            
        # Kung malaking letra ito, i-update yung tracker natin to True
        if character in upper_letters:
            has_upper_letter = True
            
    # I-return ang True kung may nakitang uppercase at walang nakitang lowercase.
    # I-return ang False kung puro numbers/symbols lang at walang letters.
    return has_upper_letter