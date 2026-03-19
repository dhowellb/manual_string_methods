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