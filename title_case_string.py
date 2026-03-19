# Function na sariling gawa para i-recreate ang .title() method
def title_case_string(target_string):
    # Reference lists para sa alphabet
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    result_string = ""
    
    # Ito yung ating "Flag" o switch. True siya sa simula dahil unang letra agad ito.
    is_start_of_word = True
    
    for character in target_string:
        # CONDITION 1: Kapag nakakita ng space...
        if character == " ":
            result_string = result_string + character
            # I-ON ulit ang switch dahil yung susunod na letra ay simula na ng bagong salita
            is_start_of_word = True
            
        # CONDITION 2: Kapag simula ito ng salita (Naka-ON ang switch)...
        elif is_start_of_word:
            # Gawing capital kung maliit na letra
            if character in lower_letters:
                for i in range(26):
                    if lower_letters[i] == character:
                        result_string = result_string + upper_letters[i]
            else:
                result_string = result_string + character
            # I-OFF na ang switch kasi tapos na yung unang letra
            is_start_of_word = False
            
        # CONDITION 3: Kapag nasa gitna o dulo na ng salita (Naka-OFF ang switch)...
        else:
            # Siguraduhing lowercase lahat
            if character in upper_letters:
                for i in range(26):
                    if upper_letters[i] == character:
                        result_string = result_string + lower_letters[i]
            else:
                result_string = result_string + character
                
    return result_string