# Function na sariling gawa para i-recreate ang .swapcase() method
def reverse_string_casing(target_string):
    # Reference lists para sa malalaki at maliliit na letra
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Dito natin iipunin yung final na salita na napagpalit na ang casing
    result_string = ""
    
    # Isa-isang i-check ang bawat character sa string
    for character in target_string:
        # CONDITION 1: Kung malaking letra siya...
        if character in upper_letters:
            # Hanapin sa alphabet at idagdag yung katumbas na maliit na letra
            for i in range(26):
                if upper_letters[i] == character:
                    result_string = result_string + lower_letters[i]
                    
        # CONDITION 2: Kung maliit na letra siya...
        elif character in lower_letters:
            # Hanapin sa alphabet at idagdag yung katumbas na malaking letra
            for i in range(26):
                if lower_letters[i] == character:
                    result_string = result_string + upper_letters[i]
                    
        # CONDITION 3: Kung space, number, o symbol, kopyahin na lang as is!
        else:
            result_string = result_string + character
            
    return result_string