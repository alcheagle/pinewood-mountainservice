from . import models

def signup(username, name, surname, email, pwdh, dob=None):
    if not alreadyIn(username):
        res = models.User.objects.create(
                username=username,
                name = name,
                surname = surname,
                email = email,
                password_hash = pwdh,
                date_of_birth = dob,
            )
        return res.id

    return None
    
def alreadyIn(username):
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return True
    else:
        return False

def getUserId(username):
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return res[0].id
    else:
        return None

def login(username, pwdh):
    res = models.User.objects.filter(
        username = username,
        password_hash = pwdh,
    )
    if res.count() == 1:
        return res[0].id
    else:
        return None

def deleteUser(username):
    pass

def getUserData(username): 
    pass

def modifyUserData(username, **kwargs):
    pass 

def createAction(action_name, description=None):
    res = models.Action.objects.filter(name = action_name)

    if res.count() == 1:
        return False
    else:
        res = models.Action.objects.get_or_create(
            name = action_name, 
            description = description,
        )
        return True
   
def modifyAction(act_name, **kwargs):
    res = models.Action.objects.filter(name = act_name)
    if res.count() == 1:
        for key in kwargs:
            if key != "name" and key != "description":
                return False

        res.update(**kwargs)
        return True
    else:
        return False

def deleteAction(name):
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        res.delete()
        return True
    else:
        return False

def getAction(name):
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        return res.values()[0]
    else:
        return None
    
    
def isAllowed(username, action):
    pass

def roleResolution(role_id): #TODO apply memoization, this needs also cache invalidation after a create or modify of role
    father_role = models.Role.objects.filter(sub_role=role_id)
    
    if father_role.count() == 1:
        res = roleResolution(father_role[0].id)
        return res.append(role_id)
    elif father_role.count() == 0:
        #this is the role father of all
        return [role_id]
    else:
        pass
        #TODO this should never happen

def actionResolution(role_id): #TODO apply memoization, this needs also cache invalidation after a create or modify of actions
    role_id_list = roleResolution(role_id)


def createRole(username, role_name, sub_role, granted_actions):
    pass

def deleteRole(username, role_name):
    pass

def modifyRole(username, role_name, actions_to_add, actions_to_delete):
    pass

def grantRole(user_granter, username, role):
    pass

def revokeRole(user_revoker, username, toRole=None):
    pass
