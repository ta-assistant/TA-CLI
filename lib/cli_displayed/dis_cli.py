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

def _massage_func(typo,massage,order):
    return f"{_display_order(order)}[{typo}] {massage}"


# public
def display_typo(order,func,massage,optional_massage="",when=False):
    typo = func
    if typo:
        print(_massage_func("/",massage,order))
    else:
        print(_massage_func("x",massage,order))
    if optional_massage != "":
        if typo == when:
            print(_massage_func("*",optional_massage,order+1))


