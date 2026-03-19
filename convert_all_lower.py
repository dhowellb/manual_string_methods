# Function na sariling gawa para i-recreate ang .lower() method
def convert_all_lower(target_string):
    # Gumawa ng reference list para sa malalaki at maliliit na letra
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Dito natin iipunin yung final na salita
    result_string = ""
    
    # Isa-isang i-check ang bawat character sa ita-type na string
    for character in target_string:
        # Kung yung character ay nasa listahan ng malalaking letra...
        if character in upper_letters:
            # Hanapin natin kung pang-ilan siya sa alphabet (0 to 25)
            for i in range(26):
                if upper_letters[i] == character:
                    # Idagdag yung katumbas niyang maliit na letra sa final string natin
                    result_string = result_string + lower_letters[i]
        else:
            # Kung space, number, o maliit na letra na siya, kopyahin na lang as is
            result_string = result_string + character
            
    return result_string