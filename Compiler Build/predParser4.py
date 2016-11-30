#python3
# predicative recursive descendent predParser by barbieAuglend


def S():
    global current_token
    if current_token == 'if':
        getNextToken()
        E()
        if current_token == 'then':
            getNextToken()
            S()
        else:
            print('Fail! expected: then token but received ', current_token)

            if current_token == 'else':
                getNextToken()
                S()
                return
            else:
                print('Fail! expected: else token but received ', current_token)

    elif current_token == 'begin':
        getNextToken()
        S()
        L()
        return

    elif current_token == 'print':
        getNextToken()
        E()
        return

    else:
        print('Fail! expected: if, begin or print token but received ', current_token)

def L():
    global current_token
    if current_token == 'end':
        return

    elif current_token == ';':
        getNextToken()
        S()
        L()
        return

    else:
        print('Fail! expected: end or ; token but received ', current_token)

def E():
    global current_token

    if current_token == 'num=num':
        getNextToken()
        return

    else:
        print('Fail! expected: end or \' num \' token but received ', current_token)

def getNextToken():
    global current_token
    global i

    i = i + 1
    current_token = user_input[i]

    while current_token not in tokens:
        i = i + 1
        current_token = user_input[i]

    return current_token



tokens = ['if', 'then', 'else', 'begin', 'print', 'end', ';', 'num=num']
user_input = list(input('Type your expression: ').split())
i = 0
current_token = user_input[i]
S()
print('Accepted!')
