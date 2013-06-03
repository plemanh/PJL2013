#Ce code récupère tous les titres des articles qui appartiennent à la catégorie Art_history parmi les 1 600 000 
#référencés sur DBpedia

import rdflib
from rdflib import Graph

g1 = Graph()
g1.parse("/Users/paullemanh/Documents/Telecom/M1/PJL/article_categories_en_uris_fr.nt", format="nt")

g2 = g1.subjects(predicate=None, object=rdflib.term.URIRef(u'http://dbpedia.org/resource/Category:Art_history'))
import pprint
for stmt in g2:
    pprint.pprint(stmt)


