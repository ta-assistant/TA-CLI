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

def _set_to_center(max_len,strvar):
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

def display_configuration(draft,workId,ta_api,number_file):
    """
    Display the configuration

    Parameter
    ---------
    draft: dict
        outputDraft and filedraft
    workId: int
    ta_api: str
        ta_api url
    number_file:
        number of file in Assignment directory
    
    Example
    -------
    >>> draft = {fileDraft: {studentId}_test.zip,outputDraft: ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
    >>> workId = 123456
    >>> ta_api = "https://ta-api.testserver.com/"
    >>> number_file = 50
    >>> display_configuration(draft,workId,ta_api,number_file)
    ... +--------------------------------------------------------------------------------------------+
    ... |                                        Configuration                                       |
    ... +--------------------------------------------------------------------------------------------+
    ... |      ta-api      |                     https://ta-api.testserver.com/                      |
    ... +--------------------------------------------------------------------------------------------+
    ... |      workId      |                                123456                                   |
    ... +--------------------------------------------------------------------------------------------+
    ... |    fileDraft     |                           {studentId}_test.zip                          |
    ... +--------------------------------------------------------------------------------------------+
    ... |   outputDraft    | ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp'] |
    ... +--------------------------------------------------------------------------------------------+
    ... | Number of files  |                                   50                                    |
    ... +--------------------------------------------------------------------------------------------+
    
    """
    outputDraft = draft["outputDraft"]
    fileDraft = draft["fileDraft"]
    dict_ele = {"ta-api": ta_api,"workId": workId,"fileDraft": fileDraft,"outputDraft": outputDraft,"Number of files": number_file}
    # find longest string
    # plus 2 becuse it's inclue 2 space |^string^|
    max_len = max([len(str(fileDraft)),len(str(outputDraft)),len(str(workId)),len(str(ta_api))])+2
    
    # line between data 
    # max_len+len("longest key name")+5 plus 5 -> 2 from longestkey's enclosed space 1 from | in the middle 
    # and last 2 from spacebar in right and left
    #example: +{space}{max_len}{space}{`|`}{longestkeyname}{space}{space}+
    new_tab_line = "+" + "-"*(max_len+len("Number of file")+5) + "+"
    setup = "|"+ _set_to_center(max_len+len("Number of file")+5,"[ Configuration ]") + "|"

    # Display table of configuration
    print(new_tab_line) 
    print(setup)
    print(new_tab_line) 
    for key, ele in dict_ele.items():
        ele = _set_to_center(max_len,ele)
        print(f"| {key:^16} |{ele}|")
        print(new_tab_line) 


    
    