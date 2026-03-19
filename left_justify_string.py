# Function na sariling gawa para gayahin ang .ljust() method (Left Justify)
def left_justify_string(target_string, target_width):
    # Kuwentahin kung ilang spaces pa ang kulang para maabot ang target width
    padding_needed = target_width - len(target_string)
    
    # Kung may kulang pa na spaces (greater than 0)...
    if padding_needed > 0:
        # Gumawa ng string na puro spaces na kasing-dami ng kulang
        added_spaces = " " * padding_needed
        # Idikit yung spaces sa kanan ng original na salita
        return target_string + added_spaces
        
    # Kung sobra o sapat na yung haba ng salita, ibalik na lang yung original nang walang pagbabago
    return target_string
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na gusto nating lagyan ng padding
    test_string = "data"
    # Target na kabuuang haba (width) na gusto nating maabot
    pad_width = 10
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = left_justify_string(test_string, pad_width)
    
    # I-print ang original at yung bagong string (gamit ang single quotes para makita ang invisible spaces)
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "' (padded)")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()