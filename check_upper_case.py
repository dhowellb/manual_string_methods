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
# Function para i-test kung gumagana yung custom logic natin sa taas
def main_execution():
    # Mag-set ng test string na gusto nating i-check
    test_string = "HELLO WORLD"
    
    # Ipasa yung string dun sa function at i-save ang True/False na sagot
    is_valid_upper = check_upper_case(test_string)
    
    # I-print ang string at kung True o False ba na naka-all caps siya
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mIs Upper:\033[0m " + str(is_valid_upper))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()