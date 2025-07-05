def main(): 

    def FizzBuzz(upTo):
        for i in range(1, upTo): 
            if i % 15 == 0: 
                print("FizzBuzz", end='')
            elif i % 5 == 0: 
                print("Buzz", end = '')
            elif i % 3 == 0: 
                print("Fizz", end ='')
            else: 
                print(f'{i}', end='')

        

if __name__=="__main__":
    main() 