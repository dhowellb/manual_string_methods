# Function na sariling gawa para gayahin ang .center() method
def center_justify_string(target_string, target_width):
    # Kuwentahin kung ilang spaces lahat ang kailangang idagdag
    padding_needed = target_width - len(target_string)
    
    # Kung may kailangang idagdag na spaces (greater than 0)...
    if padding_needed > 0:
        # Hatiin ang spaces: kalahati sa kaliwa gamit ang integer division (//)
        left_padding = padding_needed // 2
        # Yung matitirang spaces (pati butal) ay ilalagay sa kanan
        right_padding = padding_needed - left_padding
        
        # Gumawa ng string na puro spaces para sa kaliwa at kanan
        added_left_spaces = " " * left_padding
        added_right_spaces = " " * right_padding
        
        # Pagdikitin lahat: left spaces + mismong salita + right spaces
        return added_left_spaces + target_string + added_right_spaces
        
    # Kung sobra o sapat na yung haba ng salita, ibalik na lang yung original
    return target_string
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string at yung target na kabuuang haba (width)
    test_string = "hello"
    pad_width = 11
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = center_justify_string(test_string, pad_width)
    
    # I-print ang original at yung bagong string na naka-center (gamit ang single quotes para makita ang spaces)
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()