import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rdflib import Graph, Namespace

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize the text and convert to lowercase
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    return set(tokens)

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def are_graphs_identical(g1, g2):
    return len(g1) == len(g2) and all(t in g2 for t in g1) and all(t in g1 for t in g2)

def calculate_catalog_similarity(catalog1_file, catalog2_file):
    # Parse Turtle files into RDF graph
    g1 = Graph()
    g1.parse(catalog1_file, format='ttl')
    
    g2 = Graph()
    g2.parse(catalog2_file, format='ttl')
    
    # Check if the graphs are identical
    if are_graphs_identical(g1, g2):
        return 1.0
    
    # Define DCAT namespace
    dcat = Namespace('http://www.w3.org/ns/dcat#')
    
    # Extract titles and descriptions from both catalogs
    titles1 = [str(title) for title in g1.objects(predicate=dcat.title)]
    titles2 = [str(title) for title in g2.objects(predicate=dcat.title)]
    
    descriptions1 = [str(desc) for desc in g1.objects(predicate=dcat.description)]
    descriptions2 = [str(desc) for desc in g2.objects(predicate=dcat.description)]
    
    # Preprocess titles and descriptions
    titles1 = [preprocess_text(title) for title in titles1]
    titles2 = [preprocess_text(title) for title in titles2]
    descriptions1 = [preprocess_text(desc) for desc in descriptions1]
    descriptions2 = [preprocess_text(desc) for desc in descriptions2]
    
    # Calculate Jaccard similarity for titles and descriptions
    if titles1 and titles2:
        title_similarity = sum(jaccard_similarity(title1, title2) for title1 in titles1 for title2 in titles2) / (len(titles1) * len(titles2))
    else:
        title_similarity = 0.0

    if descriptions1 and descriptions2:
        description_similarity = sum(jaccard_similarity(desc1, desc2) for desc1 in descriptions1 for desc2 in descriptions2) / (len(descriptions1) * len(descriptions2))
    else:
        description_similarity = 0.0
    
    # Overall similarity as the average of title and description similarity
    overall_similarity = (title_similarity + description_similarity) / 2
    
    return overall_similarity

# Example usage:
catalog1_file = 'd1.ttl'
catalog2_file = 'd2.ttl'

similarity_score = calculate_catalog_similarity(catalog1_file, catalog2_file)
print(f"Similarity Score: {similarity_score}")
