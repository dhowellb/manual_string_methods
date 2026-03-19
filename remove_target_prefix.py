# Function na sariling gawa para tanggalin ang specific na prefix sa unahan ng text
def remove_target_prefix(target_string, prefix_string):
    # Kunin muna kung gaano kahaba yung prefix na gusto nating tanggalin
    prefix_length = len(prefix_string)
    
    # Kumuha ng sample sa unahan ng target string na kasing-haba nung prefix
    extracted_start = target_string[:prefix_length]
    
    # I-check kung nag-match ba yung kinuha nating sample sa mismong prefix
    if extracted_start == prefix_string:
        # Kung nag-match, i-chop natin yung string at i-return yung natira
        return target_string[prefix_length:]
        
    # Kung hindi nag-match, ibalik lang yung original na string nang walang pagbabago
    return target_string