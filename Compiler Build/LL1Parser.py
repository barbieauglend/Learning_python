# python 3.5
# ILL1ParsingTable {

import string
import collections


# file = grammar.txt
def read_grammar(_file):
    productions = []
    productions_options = collections.OrderedDict()

    with open(_file, 'r') as grammar_file:
        for line in grammar_file:
            line = line.replace('\n', '')
            production = line.split('->')    # Token
            terminal = production[0].strip(' ' + string.punctuation)
            non_terminals = production[1].split('|')
            for non_terminal in non_terminals:
                non_terminal = non_terminal.lstrip(' ').rstrip(' ')
                productions.append((terminal, non_terminal))
                if terminal not in productions_options:
                    productions_options[terminal] = [non_terminal]
                else:
                    productions_options[terminal] += [non_terminal]

        nonterminals = productions_options.keys()
        terminals = []

        for prod in productions:
            right_side = prod[1]
            for nonterminal in nonterminals:
                right_side = right_side.replace(nonterminal, '')
            right_side_terminals = right_side.split()
            for term in right_side_terminals:
                terminals.append(term)

        terminals = list(set(terminals))
        data = {
            'terminals': terminals,
            'nonterminals': nonterminals,
            'productions': productions,
            'production_options': productions_options,
        }
        return data


# LL1 ParsingTable
def get_production_symbols(production):
    return production.split()


def is_terminal(symbol):
    return symbol in g["terminals"]


def is_nonterminal(symbol):
    return symbol in g["nonterminals"]


def lookahead():
    global look_position
    result = string_input[look_position]
    look_position += 1
    return result


#NULLABLES
def get_nullables():
    nullables = {}
    nullables2 = nullables.copy()
    while True:  # loop until no changes
        for production in g["productions"]:
            rhs = get_rhs_of_prod(production)
            lhs = get_lhs_of_prod(production)
            if rhs == "epsilon":
                nullables[lhs] = True
            else:
                if all(is_nullable(rhs_nonterminal, nullables) and is_nonterminal(rhs_nonterminal) for rhs_nonterminal
                       in get_production_symbols(rhs)):
                    nullables[lhs] = True
        if set(nullables) == set(nullables2):
            break
        else:
            nullables2 = nullables.copy()

    return nullables


def is_nullable(symbol, nulls):
    return symbol in nulls.keys()


def get_rhs_of_prod(prod):
    return prod[1]


def get_lhs_of_prod(prod):
    return prod[0]


def is_prod_simple(rhs):
    if ' ' not in rhs:
        return True
    return False

#FIRST
def get_first_sets():
    first_sets = {}

    for terminal in g["terminals"]:
        first_sets[terminal] = {terminal}

    for non_terminal in g["nonterminals"]:
        first_sets[non_terminal] = set()

    gen = (prod for prod in g["productions"] if get_rhs_of_prod(prod) == 'epsilon')
    for prod in gen:
        lhs = get_lhs_of_prod(prod)
        first_sets[lhs].add("epsilon")

    for x in range(0, 10):
        for prod in g["productions"]:
            lhs = get_lhs_of_prod(prod)
            rhs = get_rhs_of_prod(prod)
            if not is_terminal(rhs):
                rhs = rhs.split()
                k = len(rhs)
                for i in range(0, k):
                    if rhs[i] != ' ':
                        set_be_added = first_sets[rhs[i]]
                        set_be_added -= {"epsilon"}
                        first_sets[lhs] |= set_be_added
                        if not is_nullable(rhs[i], nullables):
                            break
                if is_nullable(lhs, nullables):
                    first_sets[lhs].add("epsilon")
            else:
                first_sets[lhs].add(rhs)

    gen = (prod for prod in g["productions"] if get_rhs_of_prod(prod) == 'epsilon')
    for prod in gen:
        lhs = get_lhs_of_prod(prod)
        first_sets[lhs].add("epsilon")

    return first_sets


def get_first_set_string(string):
    return_value = set()
    if is_terminal(string):
        return_value |= first_sets[string]
        return return_value

    for i in range(len(string)):
        if string[i] != ' ':
            return_value |= first_sets[string[i]] - {"epsilon"}
            if "epsilon" not in first_sets[string[i]]:
                return return_value
    return_value.add("epsilon")
    return return_value

#FOLLOW
def get_follow_sets():
    follow_sets = {}

    for nterm in g["nonterminals"]:
        follow_sets[nterm] = set()

    starting_symbol = g["productions"][0][0]
    follow_sets[starting_symbol].add("$")

    for i in range(0, 10):
        for prod in g["productions"]:
            rhs = get_rhs_of_prod(prod)
            rhs = rhs.split()
            lhs = get_lhs_of_prod(prod)
            for i in range(0, len(rhs) - 1):
                if is_nonterminal(rhs[i]):
                    set_to_add = get_first_set_string(rhs[i + 1:]) - {"epsilon"}
                    follow_sets[rhs[i]] |= set_to_add
                    if "epsilon" in get_first_set_string(rhs[i + 1:]):
                        follow_sets[rhs[i]] |= follow_sets[lhs]
            else:
                if is_nonterminal(rhs[len(rhs) - 1]):
                    follow_sets[rhs[len(rhs) - 1]] |= follow_sets[lhs]

    return follow_sets

# PARSER
def predict_production():
    production_predict = {}

    for term in g["terminals"]:
        for nterm in g["nonterminals"]:
            production_predict[(nterm, term)] = None

    for prod in g["productions"]:
        nonterminal = get_lhs_of_prod(prod)
        rhs = get_rhs_of_prod(prod)
        for terminal in get_first_set_string(rhs):
            production_predict[(nonterminal, terminal)] = (nonterminal, rhs)
        if "epsilon" in get_first_set_string(rhs):
            for symbol in follow_sets[nonterminal]:
                production_predict[(nonterminal, symbol)] = (nonterminal, rhs)
            if "$" in follow_sets[nonterminal]:
                production_predict[(nonterminal, "$")] = (nonterminal, rhs)
    return production_predict


def pick_production(lhs, rhs):
    return predictions[(lhs, rhs)]


def match(char):
    global syntax_error
    global l
    if l == char:
        return string_input[look_position], syntax_error
    else:
        syntax_error = True
        return None, syntax_error


def match_eps():
    global syntax_error
    global l
    return string_input[look_position - 1]


def parse_initial(prod):
    global syntax_error
    parse(prod)
    if not l == string_input[-1]:
        print('Syntax error!! No possible derivation for the String ', string_input)
        return
    if syntax_error:
        print('Syntax error!! No possible derivation for the String ', string_input)
        return
    else:
        print('Accepted!!')


# testcases for grammar.txt

# string_input = "i b t a $"  # Accepted!
# string_input = "i b t i b t a $"   # Accepted
# string_input = "i b t i b t i b t a $"   # Accepted
# string_input = "i b t $"   # Syntax error
string_input = "i b t t $"   # Syntax error

# testcases for grammard.txt

# string_input = " id + id * id $"  # Accepted!
# string_input = "id * id * id $"   # Accepted
# string_input = "id + id $"   # Accepted
# string_input = "id id $"    # Syntax error


# PARSING
string_input = string_input.split()
look_position = 0

g = read_grammar('grammar.txt')

start_pos = 0
l = lookahead()

nullables = get_nullables()
first_sets = get_first_sets()
follow_sets = get_follow_sets()

syntax_error = False

predictions = predict_production()
derivation = []


def parse(prod):
    global start_pos
    global l
    global syntax_error
    global derivation

    rhsterms = get_rhs_of_prod(prod).split()
    start_pos = 0
    for term in rhsterms:
        if is_terminal(term):
            if term == "epsilon":
                l = match_eps()
                return
            else:
                l, error = match(term)
                if error:
                    return
                l = lookahead()
        else:
            prod = pick_production(term, l)
            if prod is None:
                syntax_error = True
                return
            prod_terms = prod[1].split()
            if "epsilon" in prod_terms:
                t = prod[0]
                derivation.remove(t)
            else:
                derivation = derivation[:look_position - 1] + prod_terms + derivation[look_position:]

            parse(prod)


if __name__ == '__main__':

    f = get_follow_sets()
    start = g["productions"][0][0]
    start_prod = pick_production(start, l)
    derivation.extend(start_prod[1].split())

    parse_initial(start_prod)
