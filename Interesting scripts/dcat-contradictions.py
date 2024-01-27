from rdflib import Graph

def detect_contradictions(rdf_graph):
    contradictions = set()
    subjects_predicates = {}  # Dictionary to store (subject, predicate) pairs and their corresponding objects

    # Iterate through the triples in the RDF graph and store (subject, predicate) pairs and their objects
    for subj, pred, obj in rdf_graph:
        if (subj, pred) in subjects_predicates:
            objects = subjects_predicates[(subj, pred)]
            if obj not in objects:
                contradictions.add((subj, pred))
            objects.append(obj)
        else:
            subjects_predicates[(subj, pred)] = [obj]

    return contradictions

# Example usage:
if __name__ == "__main__":
    rdf_data = """
    @prefix ex: <http://example.org/> .

    ex:John ex:hasAge 25 .
    ex:John ex:hasAge 30 .
    ex:Mary ex:hasAge 40 .
    ex:Mary ex:hasAge 30 .
    ex:Mary ex:hasAge 40 .
    """

    g = Graph()
    g.parse(data=rdf_data, format="turtle")

    contradictions = detect_contradictions(g)

    if contradictions:
        print("Contradictory statements found:")
        for subj, pred in contradictions:
            print(f"{subj} {pred}")
    else:
        print("No contradictory statements found.")

