# private
def _display_order(order,end):
    if order > 0:
        if order >1:
            set = 1
        else:
            set = 0
        if set != 0:
            order += 1
        if end:
            order = " │"*(set) + " "*order +"└─ "
        else:
            order = " │"*(set) + " "*order +"├─ "
    else:
        order = ""
    return order

def _massage_func(typo,massage,order,end):
    return f"{_display_order(order,end)}[{typo}] {massage}"


# public
def display_status_symbol(order,symbol,massage,end=False):
    """

    Display status message

    Parameter
    ---------
    order: int
        Position of message
        [0]
            [1]
                [2]
                    . . . 
    symbol: int
        0 is / , 1 is x, 3 is *
    message: str
        message that you want to show
    end: boolean
        false -> ├─

        true ->  └─
    -------
    """
    list_symbol = ["/", "x", "*"]
    print(_massage_func(list_symbol[symbol],massage,order,end))

def set_to_center(max_len,strvar):
    import math
    space = (max_len-len(str(strvar)))/2
    if space.is_integer():
        space = int(space)*" "
        strvar = space + str(strvar) + space
    else:
        space = math.ceil(space)
        space = space*" "
        strvar = space + str(strvar) + space[:-1]
    return strvar

def display_set_up(draft,workId,ta_api):
    outputDraft = draft["outputDraft"]
    fileDraft = draft["fileDraft"]
    max_len = max([len(str(fileDraft)),len(str(outputDraft)),len(str(workId)),len(str(ta_api))])+2
    dict_ele = {"ta-api": ta_api,"workId": workId,"fileDraft": fileDraft,"outputDraft": outputDraft}
    new_tab_line = "+" + "-"*(max_len+16) + "+"
    setup = "|"+ set_to_center(max_len+16,"[ SETUP ]") + "|"
    print(new_tab_line) 
    print(setup)
    print(new_tab_line) 
    for key, ele in dict_ele.items():
        ele = set_to_center(max_len,ele)
        print(f"| {key:^13} |{ele}|")
        print(new_tab_line) 


    
    