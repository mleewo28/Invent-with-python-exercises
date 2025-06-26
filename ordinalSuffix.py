
def main(): 
    def ordinalSuffix(number): 
        str_num = str(number)
        if str_num[-1] != '1' or str_num[-1] != '2' or str_num[-1] != '3' or str_num[-2] == '1':
            return str_num + "th"
        
        elif str_num[-1] == '1': 
            return str_num + "st"
        
        elif str_num[-1]=='2': 
            return str_num + "nd"
        
        elif str_num[-1] == '3': 
            return str_num + "rd" 
        
    assert ordinalSuffix(0) == '0th'

    assert ordinalSuffix(1) == '1st'

    assert ordinalSuffix(2) == '2nd'

    assert ordinalSuffix(3) == '3rd'

    assert ordinalSuffix(4) == '4th'

    assert ordinalSuffix(10) == '10th'

    assert ordinalSuffix(11) == '11th'

    assert ordinalSuffix(12) == '12th'

    assert ordinalSuffix(13) == '13th'

    assert ordinalSuffix(14) == '14th'

    assert ordinalSuffix(101) == '101st'

if __name__ == "__main__": 
    main() 
