phone_book = dict()   

def handler_add(name, number):
    phone_book[name] = number
    return

def handler_phone(name):
    for k, v in phone_book.items():
        if k == name:  
            print(f'This is phone for {k} to call: {v}')            
    return

def handler_change(name, new_number):
    if name in phone_book:
        phone_book[name] = new_number
        return       
    raise KeyError

def input_error(func):
    def inner(*args, **qwargs):
        try:
            result = func(*args, **qwargs)
            return result
        except KeyError:
            print("There is no such name in a phone book. Start again") 
        except ValueError:
            print("Input valid user name and phone")
    return inner

@input_error
def parser(input_command, input_list):
    if  input_command == 'HELLO'.lower():
        print("How can I help you?\n")
        input_command = input("Input a command from the list: add ..., change ..., phone ..., show all\n")
            
    if input_command == 'ADD'.lower():
        result = handler_add(name=input_list[1], number=input_list[2])
                
    if  input_command == 'CHANGE'.lower():
        result = handler_change(name=input_list[1], new_number=input_list[2])

    if input_command == 'PHONE'.lower():
        result = handler_phone(name=input_list[1])
                        
    if input_command == 'SHOW'.lower():
        print('Phone book: ', phone_book)
    
    return result

def main():
    while True:
        input_command = input("Input a command from the list: hello, add ..., change ..., phone ..., show all\n")
        input_list = input_command.split()

        input_command = input_list[0]

        if input_command == 'GOOD BYE'.lower() or input_command == 'CLOSE'.lower() or input_command == 'EXIT'.lower():
            print('Good bye!')
            break
        else:
            print(parser(input_command, input_list))  






