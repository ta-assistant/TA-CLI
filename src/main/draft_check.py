import os

def check_draft(path) -> bool:
    path_draft = os.path.join(path,"ta","draft.json")
    if os.path.exists(path_draft):
        return True
    else:
        return False