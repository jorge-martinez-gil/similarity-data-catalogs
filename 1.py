# Purpose: Calculate the similarity between two sets of predicates

from rdflib import Graph, URIRef

# Parse the TTL data
g = Graph()
g.parse("metadata.rdf", format="ttl")

# Get the predicates for ex:dataset-001
predicates = set()
predicates2 = set()

dataset_001 = URIRef('https://dcat.example.org/dataset-001')

for s, p, o in g.triples((dataset_001, None, None)):
    predicates.add(o)

dataset_002 = URIRef('https://dcat.example.org/dataset-002')

for s, p, o in g.triples((dataset_002, None, None)):
    predicates2.add(o)

# Calculate the similarity between the two sets of predicates item by item
similarity = 0
for p1 in predicates:
    for p2 in predicates2:
        if p1 == p2:
            similarity += 1

similarity /= max(len(predicates), len(predicates2))

print(similarity)

