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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string (halimbawa, pangalan ng file mo)
    test_string = "python_code.py"
    # Ito yung salita na gusto nating tanggalin sa unahan
    target_prefix = "python_"
    
    # Ipasa yung data dun sa custom function natin para linisin
    result_string = remove_target_prefix(test_string, target_prefix)
    
    # I-print ang pinagkaiba ng luma at bagong string
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()