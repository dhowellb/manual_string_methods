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