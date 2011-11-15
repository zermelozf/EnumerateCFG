'''
Created on Nov 14, 2011

@author: arnaud
'''

recursive_rules = ['RCsing', 'RCplur']

def causeRecursivity(prod):
    for r in recursive_rules:
        if r in [str(s) for s in prod.rhs()]:
            return 1
    return 0

def enumerate(grammar, nb_rec):
    return _enumerate(grammar, [grammar.start()], nb_rec)

def _enumerate(grammar, symbols, nb_rec):
    enum = []
    if len(symbols) == 1:
        if isinstance(symbols[0], str):
            enum.append(symbols[0])
        else:
            for prod in grammar.productions(lhs=symbols[0]):
                if causeRecursivity(prod):
                    nb_rec -= 1
                if nb_rec>= 0:
                    enum.extend(_enumerate(grammar, prod.rhs(), nb_rec))
    else:
        for first_symbol in _enumerate(grammar, [symbols[0]], nb_rec):
            for other_symbols in _enumerate(grammar, symbols[1:], nb_rec):
                    enum.append(first_symbol + ' ' + other_symbols)
    
    return enum

if __name__ == "__main__":
    import nltk
    
    grammar = nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()
    
    f = open('../enum/tong.enum','w')
    
    sentences = enumerate(grammar, 1)
    for sent in sentences[-500:]:
        print sent
    
    print len(sentences)