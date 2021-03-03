A = 'A'
B = 'B'
C = 'C'
D = 'D'

state = {}
action = None
model = {A: None, B: None, C: None, D: None} # Initially ignorant

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'NoOp'
}
rules = {
    (A, 'Dirty'):1,
    (B, 'Dirty'):1,
    (C, 'Dirty'):1,
    (D, 'Dirty'):1,
    (A, 'Clean'):2,
    (B, 'Clean'):2,
    (C, 'Clean'):2,
    (D, 'Clean'):2,
    (A, B, C, D, 'Clean'):3
}
#Ex. rule (if location == A && Dirty then rule 1)

Enviroment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}

def INTERPRET_INPUT(input): # No interpretation
    return input

def RULE_MATCH(state,rules): # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule

def UPDATE_STATE(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == model[C] == model[D] == 'Clean':
        state = (A, B, C, D, 'Clean')
        # Model consulted only for A and B clean
    model[location] = status # Update the model state 
    return state

def REFLEX_AGENT_WITH_STATE(percept):
    global state, action
    state = UPDATE_STATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = RULE_ACTION[rule]
    return action

def Sensors(): # Sense Enviroment
    location = Enviroment['Current']
    return (location, Enviroment[location])

def Actuators(action): # Modify Enviroment 
    location = Enviroment['Current']
    if action == 'Suck':
        Enviroment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Enviroment['Current'] = B 
    elif action == 'Right' and location == B: 
        Enviroment['Current'] = C
    elif action == 'Right' and location == C: 
        Enviroment['Current'] = D
    elif action == 'Right' and location == D: 
        Enviroment['Current'] = A

def run(n): # run the agent through n steps
    print('    Current                      New')
    print('Location    Status  Action  Location    Status')
    for i in range(1,n):
        (location, status) = Sensors() # Sense Enviroment before action 
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_AGENT_WITH_STATE(Sensors())
        Actuators(action)
        (location, status) = Sensors() # Sense Enviroment after action
        print("{:8s}{:12s}{:4s}".format(action, location, status))

run(20)