import re

def read_template(file_path):
    with open(file_path, mode='r') as f:
        res = f.read()
        print(res)
        return res

def parse_template(input_str):
    expected_parts = tuple(re.findall(r"{([^}]+)}", input_str))
    expected_stripped = re.sub(r"{([^}]+)}", "{}", input_str)
    
    # expected_parts = tuple(re.findall(r"\{(\w+)\}", input_str))
    # expected_stripped = re.sub(r"\{(\w+)\}", "{}", input_str)
    
    return expected_stripped, expected_parts

def merge(before, input_list):
    after = before.format(*input_list)
   
    return after

def intro():
    print('''
**************************************
**    Welcome to the madlib game   **
**    Please enter 21 words and write them
       as prompted.                   **
**
** To quit at any time, type "quit" **
**************************************
''')

def user_input(word,number):
    user_input = input(f"this input {number}from 21 {word}>")
    return user_input

def addFile(result):
    with open('assets/write.txt', mode='w') as f : 
        f.write(result)

def main():
    intro()
    template = read_template("/home/ibrahim/madlib-cli/assets/madlib-cli.txt")
    expected_stripped, expected_parts = parse_template(template)
    user_inputs = []
    number=0
    for word in expected_parts:
        number = 1+number
        user_word = user_input(word,number )
        user_inputs.append(user_word)
    result = merge(expected_stripped, user_inputs)
    print(result)
    addFile(result)
    end_application()

def end_application():
    print("Thanks for playing the madlib game!")

if __name__ == "__main__":
    main()
