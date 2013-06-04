#Ce code recupere tous les titres des articles qui appartiennent a la categorie uri_cat parmi les 1 600 000 
#references sur DBpedia

import rdflib
from rdflib import Graph

uri_cat = rdflib.term.URIRef(u'http://dbpedia.org/resource/Category:Art_history')
g1 = Graph()
g2 = Graph()
g1.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/article_categories_en_uris_fr.nt", format="nt")
g2.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/long_abstracts_en_uris_fr.nt", format="nt")

g3 = g1.subjects(predicate=None, object=uri_cat)

import os

f=str(uri_cat)
f=f.split(':')
f=f[-1]

try:
    os.mkdir('/Users/paullemanh/Documents/Telecom/M1/PJL/%s' % f)
except OSError:
    pass
    
for stmt in g3:
    g4 = g2.objects(subject=stmt, predicate=None)
    
    for stmt2 in g4:
        
        f2 = str(stmt)
        f2=f2.split('/')
        f2=f2[-1]
        fich=open('/Users/paullemanh/Documents/Telecom/M1/PJL/{0}/{1}'.format(f,f2),'w')
        fich.write(stmt2.encode('utf-8'))
        
    pass
pass



