class error(Exception):
    pass
class InputTooSmall(error):
    pass
class InputTooLarge(error):
    pass
alpha = 'k'
while True:
    try:
        apb=input("Enter an alphbet")
        if apb < alpha:
            raise InputTooSmall
        elif apb > alpha:
            raise InputTooLarge
        break
    except InputTooSmall:
        print("The Entered alphabet is too small ,try again")
        print('')
    except InputTooLarge:
        print("The Entered alphabet is too large,try again")
        print('')
print("Congratulations ! you guessed it correctly")        