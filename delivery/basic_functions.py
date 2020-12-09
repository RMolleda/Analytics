def append_item(item, where):
    """
    U must set the object u want to append as the value of "object" 
    and "where" should be the list where u want to append it
    """
    where.append(item)

def remove_item_list(item, where):
    """
    pop the input from a list 
    it will loop arround all the list, and if the item is on it, it will be removed from the list
    """
    while True:        
        if item in where:
            where.remove(item)
        else:
            break

def suma(*args):
    return sum(args)
 
    

