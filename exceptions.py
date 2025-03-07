#exceptions - try, except, finally
#single inheritance/multiple inheritance
#graphical user interface
#turtle module


#you can have multiple try-blocks
#question on for, while with else

##error = True
##
##while error:  #using a while-else structure rather than break 
##    try:
##        value1 = int(input('Enter numerator:'))
##        value2 = int(input('Enter denominator:'))
##
##        ans = value1/value2
##
##    except ValueError:
##        print('Wrong value entered: integer expected')
##
##    except ZeroDivisionError as msg:
##        print(msg)
##
##    except:
##        print('Some other error has occured.')
##
##    else:
##        print(f'{value1}/{value2} = {ans}')
##        error = False
##                 
#you can create your own exceptions via inheritance

class deezNuts(Exception):
    pass
    
try:
    name = input('Enter your name:').strip()
    if name == 'Jeremiah':
        raise deezNuts

except deezNuts:
    print(f'I just don\'t like your face.')
    print('Very unfortunate.')
    
    
