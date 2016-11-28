from . import models

#Create a new user with username (unique), name, surname, email (unique), hash
#password and an optional date of birth. If the user already exists it return
#None, otherwise it returns the id of the new user.
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

#Check if the user already exists. Returns True if it does exists, false
#otherwise
def alreadyIn(username):
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return True
    else:
        return False

#Given the username it returns the id where that user exists
def getUserId(username):
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return res[0].id
    else:
        return None

#Get username and password hash to check if the user exists, and in this case
#it returns the id
def login(username, pwdh):
    res = models.User.objects.filter(
        username = username,
        password_hash = pwdh,
    )
    if res.count() == 1:
        return res[0].id
    else:
        return None

#Given the username, checks id that user exists and eventually deletes it
def deleteUser(username):
    pass

#Returns all the data of a user if it exists
def getUserData(username):
    pass

#Get a dictionary containing the new data for a certain user
def modifyUserData(username, **kwargs):
    pass

#Create a new action with description (optionally) if the name of the going-to-be
#action isn't already being used. Returns true if the action was created, False
#otherwise
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

#Given the name and a dictionary containing the new data for that action, it
#modify the action values. Returns True if the change went well, False otherwise
#and False if the action doesn't exist too.
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

#Check if the given action exists and delete it in case. Returns True if it was
#successfully erased, False otherwise
def deleteAction(name):
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        res.delete()
        return True
    else:
        return False

#Check if the given action exists, and in case it does, the function returns
#a dictionary containing the values of the action, otherwise it returns None
def getAction(name):
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        return res.values()[0]
    else:
        return None

#Check if the given user is allowed to accomplish a certain action.
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


#Create a new Role. It has to check that the user who wants to create it is
#allowed to. It then create a new sub_role which will be granted the possibility
#of accomplishing certain actions.
def createRole(username, role_name, sub_role, granted_actions):
    pass

#Check if a certain role exists, then check if the user is allowed to delete it
#and eventually delete it.
def deleteRole(username, role_name):
    pass

#Check if a certain role exists, then check if the user is allowed to modify it
#and eventually modify it.
def modifyRole(username, role_name, actions_to_add, actions_to_delete):
    pass

#Check if the granter has the possibility to promote a certain user, and
#eventually it does
def grantRole(user_granter, username, role):
    pass

#Check if the granter has the possibility to revoke a certain role from a user,
#and eventually it does
def revokeRole(user_revoker, username, toRole=None):
    pass
