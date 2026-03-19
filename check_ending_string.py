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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na gusto nating i-check
    test_string = "computer engineering"
    # Ito yung salita na inaasahan nating nasa dulo
    target_suffix = "engineering"
    
    # Ipasa yung data dun sa custom function at i-save ang True/False na resulta
    is_match = check_ending_string(test_string, target_suffix)
    
    # I-print ang original string at kung nag-match ba yung target suffix
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mEnds with target:\033[0m " + str(is_match))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()