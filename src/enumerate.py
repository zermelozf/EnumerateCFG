'''
Created on Nov 10, 2011

@author: arnaud
'''

def enumerate(grammar):
    return _enumerate(grammar, [grammar.start()])

def _enumerate(grammar, symbols):
    enum = []
    if len(symbols) == 1:
        if isinstance(symbols[0], str):
            enum.append(symbols[0])
        else:
            for prod in grammar.productions(lhs=symbols[0]):
                enum.extend(_enumerate(grammar, prod.rhs()))
    else:
        for first_symbol in _enumerate(grammar, [symbols[0]]):
            for other_symbols in _enumerate(grammar, symbols[1:]):
                enum.append(first_symbol + ' ' + other_symbols)
    return enum

if __name__ == "__main__":
    import nltk
    
    grammar = nltk.parse.load_parser('file:../grammars/simple.cfg').grammar()
    
    sentences = enumerate(grammar)
    for sent in sentences:
        print sent
    
    print len(sentences)