#Ce code recupere tous les titres des articles qui appartiennent a la categorie uri_cat et aux categories "n-1"
#parmi les articles de DBpedia


import rdflib
from rdflib import Graph

g1 = Graph()
g2 = Graph()
g5 = Graph()
g1.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/article_categories_en_uris_fr.nt", format="nt")
g2.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/long_abstracts_en_uris_fr.nt", format="nt")
g5.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/skos_categories_en_uris_fr.nt", format="nt")

uri_cat = rdflib.term.URIRef(u'http://dbpedia.org/resource/Category:Religion')
g3 = g1.subjects(predicate=None, object=uri_cat)
g6 = g5.subjects(predicate=rdflib.term.URIRef(u'http://www.w3.org/2004/02/skos/core#broader'), object=uri_cat)


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

for stmt3 in g6:
        
        g3 = g1.subjects(predicate=None, object=stmt3)
        
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
    
pass



