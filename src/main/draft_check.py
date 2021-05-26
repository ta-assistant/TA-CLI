import os

def check_draft(path: str) -> bool:
    """
    check draft.json that exist or not
<<<<<<< HEAD

    Args:
        path (str): path of work directory

=======
    Args:
        path (str): path of work directory
>>>>>>> master
    Returns:
        bool: if draft.json exists return true else false
    """
    path_draft = os.path.join(path,"ta","draft.json")
    if os.path.exists(path_draft):
        return True
    else:
        return False