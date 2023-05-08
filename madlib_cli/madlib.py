def read_template(n):
    '''this function reads the file 
       using the path provided and
       returns its content if it exists
       otherwise it raises and error
      '''
    try:
        with open( n, mode='r') as f : 
            res = f.read()
            print(res)  
            return res
    except  FileNotFoundError :   
            raise FileNotFoundError("")

def parse_template(input_str):
    '''this function takes the file content and 
    removes the parts inside of curly brackets
    then return them in a tuple
    '''
    
    import re
    expected_stripped = tuple(re.findall(r"\{(\w+)\}", input_str))
    expected_parts = re.sub(r"\{(\w+)\}", "{}", input_str)
    return expected_parts ,expected_stripped

def merge(befor,input):
    '''this function merges the game template with the user input and returns
    the template filled with the input
    '''
    befor=f"{befor}"
    after =befor.format(*input)    
    print (after)
    return after





def intro():
    print('''
**************************************
**    Welcome to the madlib game   **
**    Please in 21 word and add write it 
      when you  asked.    **
**

**************************************


''')

def user_insertion():
    user_input=input(">")  
    return user_input       

def main():
    # user_input = user_insertion()
    # thislist = [] 
    # my_count = {}
    res= read_template("./assets/madlib-cli.txt")
    parsing=parse_template(res) 
    mergee =merge(parsing[0],parsing[1] )
    print(parsing[0],"heeer1")
    print(parsing[1],"heeeer")
    print(mergee)
    end_application()


def end_application():
    print("thanks for using snakes cafe application !")          


if __name__=="__main__": 
    intro()  
    main()
                 