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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na gulo-gulo ang casing
    test_string = "PyThOn CoDe"
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = reverse_string_casing(test_string)
    
    # I-print ang original at yung bagong string na naka-swap na ang case
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()