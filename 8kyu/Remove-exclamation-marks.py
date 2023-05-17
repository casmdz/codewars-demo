#Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    old_str = s
    new_str = old_str.replace("!", "")
    
    return new_str