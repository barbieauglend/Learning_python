#python3
# predicative recursive descendent predParser by barbieAuglend

def T():
    global current_token

    if current_token == 'program':
        getNextToken()
        S()
        if current_token == 'end':
            return
        else:
            print('Fail! expected: end token but received ', current_token)

    else:
        print('Fail! expected: \' program \' token but received ', current_token)

def S():
    global current_token
    if current_token == 'if':
        getNextToken()
        E()
        if current_token == 'then':
            getNextToken()
            S()
            E()
            return
        else:
            print('Fail! expected: then token but received ', current_token)

    elif current_token == 'begin':
        getNextToken()
        S()
        if current_token == 'end':
            return
        else:
            print('Fail! expected: end token but received ', current_token)

    elif current_token == 'epsilon':
        getNextToken()
        return

    else:
        print('Fail! expected: if, begin or \' \' token but received ', current_token)

def E():
    global current_token
    if current_token == 'else':
        getNextToken()
        if current_token =='fi':
            return
        else:
            print('Fail! expected: fi token but received ', current_token)

    elif current_token == 'fi':
        return

    else:
        print('Fail! expected: else or fi token but received ', current_token)

def getNextToken():
    global current_token
    global i

    i = i + 1
    current_token = user_input[i]

    while current_token not in tokens:
        i = i + 1
        current_token = user_input[i]

    return current_token



tokens = ['program', 'end', 'if', 'then', 'begin', 'epsilon', 'else', 'fi']
user_input = list(input('Type your expression: ').split())
i = 0
current_token = user_input[i]
T()
print('Accepted!')
