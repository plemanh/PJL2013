#Ce code recupere tous les titres des articles qui appartiennent a la categorie Art_history parmi les 1 600 000 
#references sur DBpedia

import rdflib
from rdflib import Graph

g1 = Graph()
g1.parse('/Users/Louis/Desktop/PJL2013/donnee/donneuri.nt', format="nt")

g2 = g1.subjects(predicate=None, object=rdflib.term.URIRef(u'http://dbpedia.org/resource/Category:Art_history'))

import pprint
for stmt in g2:
    pprint.pprint(stmt)


