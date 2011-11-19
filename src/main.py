'''
Created on Nov 15, 2011

@author: arnaud
'''
import nltk
import random
from enumerate_small_sentences import enumerate
    
grammar = nltk.parse.load_parser('file:../grammars/tong.cfg').grammar()

max_len = 3
f = open('../enum/tong'+str(max_len)+'words.enum','w')

sentences = enumerate(grammar, max_len)
for sent in sentences:  
    f.write(sent+'\n')    

print 'cat hits girl who sees .' in sentences
print 'cat who girl hits lives .' in sentences

#print sentences

for i in [random.randint(0,len(sentences)-1) for k in range(10)]:
    print sentences[i]

print ""
print "Number of sentences:", len(sentences)    
print "Max_lenght =", max([len(s.split(' ')) for s in sentences])

#for k in range(10):
#    f = open('../enum/set'+str(k)+'_maxlen'+str(max_len),'w')
#    print "Creating set", k
#    for l in range(10000):
#        f.write(sentences.pop(random.randint(0,len(sentences)-1))+'\n')