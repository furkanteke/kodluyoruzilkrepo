def flattener(userlist):
    condition=True
    while condition:
        condition=False
        for listindex,value in enumerate(userlist):
            if type(value)==list:
                condition=True
                for subindex,subvalue in enumerate(value):
                    userlist.insert(listindex+subindex,subvalue)
                userlist.remove(value)
    return userlist

def reverselist(userlist):
    for listindex,value in enumerate(userlist):
        if type(value)==list:
            userlist[listindex]=value[::-1]
    return userlist[::-1]

    
