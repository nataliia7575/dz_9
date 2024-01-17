phone_book = dict()   

def input_error(func):
    def inner(*args, **qwargs):
        try:
            result = func(*args, **qwargs)
            return result
        except KeyError:
            print("There is no such name in a phone_book. Start again") 
            return 

    return inner

def message_parser(input_message):
    name, phone = input_message.split()
    return name, phone

def handler_add():
    try:
        input_message = input("Input new contact: name and phone \n")
        name, phone = message_parser(input_message)
        phone_book[name] = phone
    except ValueError:
        print("Input valid user name and phone")
    return

def handler_phone():
    input_message = input("Input contact name to get a phone to call:\n")
    name = input_message
    for k, v in phone_book.items():
        if k == name:  
            print(f'This is phone for {k} to call {v}')            
    return

@input_error
def handler_change():
    try:
        input_message = input("Input contact name and new phone to be changed:\n")
        name, phone = message_parser(input_message)
        print(f'Changing phone for {phone_book[name]}')
        phone_book[name] = phone   
    except ValueError:
        print("Input valid user name and phone: ")             
    return

def main():
    while True:
        input_command = input("Input a command from the list: hello, add, change, phone, show all\n").lower()

        if input_command == 'HELLO'.lower():
            print("How can I help you?\n")
            input_command = input("Input a command from the list: add, change, phone, show all\n")
            
        if input_command == 'ADD'.lower():
            result= handler_add()
                   
        if input_command == 'CHANGE'.lower():
            result= handler_change()

        if input_command == 'PHONE'.lower():
            result= handler_phone()
                           
        if input_command == 'SHOW ALL'.lower():
            print('Phone book: ', phone_book)

        if input_command == 'GOOD BYE'.lower() or input_command == 'CLOSE'.lower() or input_command == 'EXIT'.lower():
            print('Good bye!')
            break
    return result

print(main())






