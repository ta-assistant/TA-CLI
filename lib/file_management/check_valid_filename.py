import os, json

def check_extension(draft):
    remainder = ""
    for i in draft[::-1]:
        if i == ".":
            extension = (remainder + i)[::-1]
            break
        remainder += i
    return extension

    
def check_draft_file(draft):
    key = []
    for i in draft:
        if i == "{":
            remainder = ""
        elif i == "}":
            key.append(remainder)
        else:
            remainder += i
    return key


def check_file_name(path,filename,draft):
    extension = check_extension(draft)
    if extension not in filename:
        return False
    list_filename = filename[:-len(extension)].split("_")
    list_draft = check_draft_file(draft)
    for key,value in zip(list_draft,list_filename):
        if key == "ID":
            try:
                int(value)
            except ValueError:
                return False
    return True
    
    

