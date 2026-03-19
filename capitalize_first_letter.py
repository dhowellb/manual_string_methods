# Function na sariling gawa para i-recreate ang .capitalize() method
def capitalize_first_letter(target_string):
    # EDGE CASE: Kung walang laman yung string, ibalik agad para hindi mag-error
    if len(target_string) == 0:
        return target_string
        
    # Reference lists para sa alphabet
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Hatiin ang string: kunin yung pinakaunang letra, at yung natitirang bahagi
    first_character = target_string[0]
    rest_of_string = target_string[1:]
    
    # STEP 1: Gawing capital yung unang letra (kung maliit siya)
    capitalized_first = first_character
    if first_character in lower_letters:
        for i in range(26):
            if lower_letters[i] == first_character:
                capitalized_first = upper_letters[i]
                
    # STEP 2: Gawing lowercase yung natitirang bahagi ng string
    lowered_rest = ""
    for character in rest_of_string:
        if character in upper_letters:
            for i in range(26):
                if upper_letters[i] == character:
                    lowered_rest = lowered_rest + lower_letters[i]
        else:
            lowered_rest = lowered_rest + character
            
    # Pagdikitin yung naka-capital na unang letra at yung naka-lowercase na natitira
    return capitalized_first + lowered_rest
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na gulo-gulo ang casing
    test_string = "hELLO wORLD"
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = capitalize_first_letter(test_string)
    
    # I-print ang original at yung bagong string na naka-capitalize na
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()