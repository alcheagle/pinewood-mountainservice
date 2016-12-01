from . import models

def signup(username, name, surname, email, pwdh, dob=None):
    '''
    Create a new user with username (unique), name, surname, email (unique), hash password and an optional date of birth. If the user already exists it return None, otherwise it returns the id of the new user.
    '''
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
    '''
    Check if the user already exists. Returns True if it does exists, false
    otherwise
    '''
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return True
    else:
        return False

def getUserId(username):
    '''
    Given the username it returns the id where that user exists
    '''
    res = models.User.objects.filter(username=username)

    if res.count() == 1:
        return res[0].id
    else:
        return None

def login(username, pwdh):
    '''
    Get username and password hash to check if the user exists, and in this case it returns the id
    '''
    res = models.User.objects.filter(
        username = username,
        password_hash = pwdh,
    )
    if res.count() == 1:
        return res[0].id
    else:
        return None

def deleteUser(username):
    '''
    Given the username, checks id that user exists and eventually deletes it. Returns True if the user existed and it was deleted, False if it didn't exists.
    '''
    res = models.User.objects.filter(username = username)

    if res.count() == 1:
        res.delete()
        return True
    else:
        return False

def getUserData(username):
    '''
    Returns all the data of a user if it exists. It returns None if the user wasn't found
    '''
    res = models.Action.objects.filter(username = username)

    if res.count() == 1:
        return res.values()[0]
    else:
        return None

def modifyUserData(username, **kwargs):
    '''
    Get a dictionary containing the new data for a certain user. It returns False whether the user wasn't found nor the dictionary had the right keys. It returns True if the change went well.
    '''
    res = models.Action.objects.filter(username = username)

    if res.count() == 1:
        for key in kwargs:
            if key != "name" and key != "surname" and key != "username" and key != "email" and key != "date_of_birth" and key != "password_hash" and key != "role":
                return False
        res.update(**kwargs)
        return True
    else:
        return False

def createAction(action_name, description=None):
    '''
    Create a new action with description (optionally) if the name of the going-to-be action isn't already being used. Returns true if the action was created, False otherwise
    '''
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
    '''
    Given the name and a dictionary containing the new data for that action, it modify the action values. Returns True if the change went well, False otherwise and False if the action doesn't exist too.
    '''
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
    '''
    Check if the given action exists and delete it in case. Returns True if it was successfully erased, False otherwise
    '''
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        res.delete()
        return True
    else:
        return False

def getAction(name):
    '''
    Check if the given action exists, and in case it does, the function returns a dictionary containing the values of the action, otherwise it returns None
    '''
    res = models.Action.objects.filter(name = name)

    if res.count() == 1:
        return res.values()[0]
    else:
        return None

def isAllowed(username, action):
    '''
    Check if the given user is allowed to accomplish a certain action.
    '''
    res = models.User.objects.get(username=username)


def roleResolution(role_id): #TODO apply memoization, this needs also cache invalidation after a create or modify of role
    def roleres_aux(role_id, res=[]): #TODO check the correctness of the queries
        father_role = models.Role.objects.get(id=role_id)
        res.append(role_id)
        if father_role.count() == 1:
            roleres_aux(father_role[0].super_role, res)
        elif father_role.count() == 0:
            #this is the role father of all
            return res
        else:
            pass
            #CHECK this should never happen

    return roleres_aux(role_id)

def actionResolution(role_id): #TODO apply memoization, this needs also cache invalidation after a create or modify of actions
    role_id_list = roleResolution(role_id)

    res = Role.objects.select_related().filter(id__in=role_id_list) #TODO check if this provides what desired

    #return [x["actions"] for x in res.values()]

def createRole(username, role_name, super_role, granted_actions):
    '''
    Create a new Role. It has to check that the user is allowed to create it. It then create a new super_role which will be granted the possibility of accomplishing certain actions.
    '''
    res = models.Role.objects.filter(name = role_name)

    if res.count() == 1:
        return False
    else:
        res = models.Role.objects.get_or_create(
            name = role_name,
            super_role = super_role,
            actions = [createAction(action) for action in granted_actions], #TODO check if right
        )
        return True

def deleteRole(username, role_name):
    '''
    Check if a certain role exists, then check if the user is allowed to delete it and eventually delete it.
    '''
    res = models.Role.objects.filter(name = role_name)

    if res.count() == 1:
        if isAllowed(username, 'deleteRole'):
            res.delete()
            return True
        else:
            return False
    else:
        return False

def modifyRole(username, role_name, actions_to_add, actions_to_delete):
    '''
    Check if a certain role exists, then check if the user is allowed to modify it and eventually modify it.
    '''
    res = models.Role.objects.filter(name = role_name)
    if res.count() == 1:
        for key in kwargs:
            if key != "name" and key != 'super_role' and key != "actions":
                return False
        res.update(**kwargs) #TODO NOT SO FUCKING SURE
        return True
    else:
        return False


def grantRole(user_granter, username, role):
    '''
    Check if the granter has the possibility to promote a certain user, and eventually it does
    '''
    pass

def revokeRole(user_revoker, username, toRole=None):
    '''
    Check if the granter has the possibility to revoke a certain role from a user, and eventually it does
    '''
    pass
