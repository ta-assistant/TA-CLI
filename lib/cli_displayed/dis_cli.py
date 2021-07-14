def display_order(order):
    if order > 0:
        if order >1:
            set = 1
        else:
            set = 0
        order = " |"*(set) + " "*order +"|-"
    else:
        order = ""
    return order

    
def display_typo(order,func,massage,optional_massage="",when=False):
    typo = func
    if typo:
        print(massage_func("/",massage,order))
    else:
        print(massage_func("x",massage,order))
    if optional_massage != "":
        if typo == when:
            print(massage_func("*",optional_massage,order+1))


def massage_func(typo,massage,order):
    return f"{display_order(order)}[{typo}] {massage}"