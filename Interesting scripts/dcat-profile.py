from rdflib import Graph, Literal, XSD, Namespace

def check_data_types(rdf_data):
    
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    ex = Namespace("http://example.org/")
    
    graph = Graph().parse(data=rdf_data, format="turtle")
    incorrect_data_types = set()

    # Define a dictionary to map predicates to their expected data types

    predicate_data_types = {
        "<http://example.org/hasAge>": XSD.decimal,
        "<http://example.org/hasHeight>": XSD.decimal,
        # Add more predicate-data type mappings as needed
    }

    for subj, pred, obj in graph:
        print(pred)
        print(predicate_data_types)
        print (pred in predicate_data_types)
        if f"<{pred}>" in predicate_data_types:
            expected_data_type = predicate_data_types[f"<{pred}>"]
            if isinstance(obj, Literal) and obj.datatype != expected_data_type:
                incorrect_data_types.add((subj, pred))

    return incorrect_data_types

# Example usage:
if __name__ == "__main__":
    rdf_data = """
    @prefix ex: <http://example.org/> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    ex:Mary ex:hasAge "40"^^xsd:integer .
    ex:Peter ex:hasHeight "5.9"^^xsd:decimal .
    """

    incorrect_data_types = check_data_types(rdf_data)

    if incorrect_data_types:
        print("Incorrect data types found:")
        for subj, pred in incorrect_data_types:
            print(f"{subj} {pred}")
    else:
        print("No incorrect data types found.")