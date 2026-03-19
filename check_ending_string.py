# Function na sariling gawa para i-recreate ang .endswith() method
def check_ending_string(target_string, suffix_string):
    # Kunin muna ang haba ng hinahanap nating salita sa dulo
    suffix_length = len(suffix_string)
    
    # EDGE CASE 1: Kung walang nilagay na hahanapin, automatic True (dahil lahat naman may empty string sa dulo)
    if suffix_length == 0:
        return True
        
    # EDGE CASE 2: Kung mas maikli yung mismong target kaysa sa hinahanap, impossible na mag-match. False agad!
    if len(target_string) < suffix_length:
        return False
        
    # Kumuha ng sample sa dulo ng target string gamit ang negative slicing
    extracted_end = target_string[-suffix_length:]
    
    # I-check kung nag-match ba yung kinuha nating sample sa dulo dun sa mismong hinahanap natin
    if extracted_end == suffix_string:
        return True
        
    # Kung hindi nag-match, ibig sabihin iba ang dulo niya
    return False