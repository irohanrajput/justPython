def outer_function(msg):
    message = msg
    
    def inner_function():
        print (message)
    return inner_function()

hi_func = outer_function('hii')
bye_func = outer_function('bye')yyyyy