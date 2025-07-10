def every15Minutes(): 
    for i in ['am','pm']:
        for j in ['12','1','2','3','4','5','6','7','8','9','10','11']:
            for k in ['00','15','30','45']:
                print(f"{j}:{k} {i}")

every15Minutes()