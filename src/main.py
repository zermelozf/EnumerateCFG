'''
Created on Nov 15, 2011

@author: arnaud
'''
import nltk
import random
from enumerate_small_sentences import enumerate
import cPickle as pickle
    
grammar = nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()

max_len = 8
f = open('../enum/tong'+str(max_len)+'words.enum','w')

sentences = enumerate(grammar, max_len)
   
pickle.dump(sentences, f)

for i in [random.randint(0,len(sentences)-1) for k in range(10)]:
    print sentences[i]

print ""
print "Number of sentences:", len(sentences)    
print "Max_lenght =", max([len(s) for s in sentences])
