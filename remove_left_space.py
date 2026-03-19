# Function na sariling gawa para tanggalin ang spaces sa kaliwa (custom .lstrip)
def remove_left_space(target_string):
    # Simulan ang pagbibilang sa index 0 (pinakaunang character)
    start_index = 0
    
    # Habang hindi pa tayo lumalagpas sa haba ng string AT space (" ") ang nakikita natin...
    while start_index < len(target_string) and target_string[start_index] == " ":
        # I-usog lang nang i-usog ang index natin pakaliwa
        start_index = start_index + 1
        
    # I-return yung string simula doon sa unang hindi-space na character (string slicing)
    return target_string[start_index:]
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na may spaces sa simula
    test_string = "   hello world"
    
    # Ipasa yung test string dun sa custom function natin para linisin
    result_string = remove_left_space(test_string)
    
    # I-print ang pinagkaiba ng luma at bagong string (may single quotes para halata yung spaces)
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()