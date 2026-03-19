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