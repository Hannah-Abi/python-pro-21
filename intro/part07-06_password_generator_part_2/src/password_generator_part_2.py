# Write your solution here
import random
import string
def generate_strong_password(amount:int, num: bool, cha: bool):
    i = 0
    password = ""
    # required symbols
    symbols = ('!', '?', '#', '=', '-', '+', '(', ')')
    if num == False and cha == False:
        choice = random.choices(string.ascii_lowercase, k = amount)
        for i in range(len(choice)):
            password += choice[i]
    if num == True and cha == False:
        number_of_num = random.randint(1,amount-1)
        chosen_numbers = random.choices(string.digits, k = number_of_num)
        number_of_leters = amount-number_of_num
        chosen_letters = random.choices(string.ascii_lowercase, k = number_of_leters)
        password_e_list = chosen_letters + chosen_numbers
        random.shuffle(password_e_list)
        password = ''.join(password_e_list)
    if num == False and cha ==True:
        number_of_symbol = random.randint(1,amount-1)
        chosen_symbols = random.choices(symbols, k = number_of_symbol)
        number_of_leters = amount-number_of_symbol
        chosen_letters = random.choices(string.ascii_lowercase, k = number_of_leters)
        password_e_list = chosen_letters + chosen_symbols
        random.shuffle(password_e_list)
        password = ''.join(password_e_list)
    if num == True and cha == True:
        number_of_num = random.randint(1,amount-2)
        chosen_numbers = random.choices(string.digits, k = number_of_num)
        number_of_symbol = random.randint(1,amount-number_of_num-1)
        chosen_symbols = random.choices(symbols, k = number_of_symbol)
        number_of_leters = amount-number_of_symbol - number_of_num
        chosen_letters = random.choices(string.ascii_lowercase, k = number_of_leters)
        password_e_list = chosen_letters + chosen_symbols +chosen_numbers
        random.shuffle(password_e_list)
        password = ''.join(password_e_list)
    return password 

if __name__=="__main__":
    for i in range(10):
        #print(generate_strong_password(8, True, False))
        #print(generate_strong_password(2, False, False))
        print(generate_strong_password(8, False, True))
        #print(generate_strong_password(5, False, True))
        