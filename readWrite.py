def main(): 
    outfile = open("greet.txt", "w")
    #Write to greet.txt
    outfile.write('Hello!\n')
    #Append to greet.txt

    outfile = open("greet.txt", "a")
    outfile.write('Goodbye!\n')

    # with open('greet.txt','a') as outfile: 
    #     outfile.write('Goodbye!\n')
    
    
    outfile.close()

if __name__ =="__main__":
    main()