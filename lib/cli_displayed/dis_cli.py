"""
Display typo

============

A simple function to displayed the working process to user.
You should use this function on every process on this program to be the standard of this project.

Limitations
-----------
This function can display maximum of 2 line first is main line and second is optional line.
And the typo is depend on the boolean variable, so it have only 2 typo [/] and [x]


"""

# private
def _display_order(order):
    if order > 0:
        if order >1:
            set = 1
        else:
            set = 0
        order = " |"*(set) + " "*order +"|-"
    else:
        order = ""
    return order

def _message_func(typo,message,order):
    return f"{_display_order(order)}[{typo}] {message}"


# public
def display_typo(order,func,message,optional_message="",when=False):
    """
    Use this function for displayed process on user screen

    Args:
        order (int): 
            order the position in line
            [0]
                [1]
                    [2] . . .

        func (bool): 
            boolean to tell that it's pass or not

        message (str): 
            string to displayed to the user screen
            [?] <message>

        optional_message (str): Defaults to ""
            if this include it will displayed in order+1 position
            [?] <main message>
                [*] <optional message>

        when (bool): Defaults to False.
            if this var is equal to `func` optional message will be displayed
    
    Notes
    -----
    you can pass function that return boolean into func 

    =========
    def func1():
        return False

    >>> display_typo(0,func1(),"message")
    ... [x] message
    =========

    example
    -------

    >>> display_typo(0,True,"message")
    ... [/] message

    >>> display_typo(0,False,"message")
    ... [x] message

    >>> display_typo(0,True,"message","optional_message",when=True)
    ... [/] message
    ... |-[*] optional_message

    >>> display_typo(0,True,"message","optional_message",when=False)
    ... [/] message

            
    """
    typo = func
    if typo:
        print(_message_func("/",message,order))
    else:
        print(_message_func("x",message,order))
    if optional_message != "":
        if typo == when:
            print(_message_func("*",optional_message,order+1))


