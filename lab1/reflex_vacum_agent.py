A = 'A'
B = 'B'
C = 'C'
D = 'D'

Enviroment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}

def REFLEX_VACUUM_AGENT(loc_st): #Determine action
    if loc_st[1] == 'Dirty':
        return 'suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Right'
    if loc_st[0] == C:
        return 'Right'
    if loc_st[0] == D:
        return 'Right'

def Sensors(): # Sense Enviroment
    location = Enviroment['Current']
    return (location,Enviroment[location])

def Actuators(action): # Modify Enviroment
    location = Enviroment['Current']
    if action == 'suck':
        Enviroment[location] = 'clean'
    elif action == 'Right' and location == A:
        Enviroment['Current'] = B
    elif action == 'Right' and location == B:
        Enviroment['Current'] = C
    elif action == 'Right' and location == C:
        Enviroment['Current'] = D
    elif action == 'Right' and location == D:
        Enviroment['Current'] = A

def run(n, REFLEX_VACUUM_AGENT): # run the agent through n steps
    print('     Current                       New')
    print('location     status  action  location   status')
    for i in range(1,n):
        (location, status) = Sensors() # Sense Enviroment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors() # Sense Eviroment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))

run(20,REFLEX_VACUUM_AGENT)