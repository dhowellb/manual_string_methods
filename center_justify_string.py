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