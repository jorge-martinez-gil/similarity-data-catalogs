import streamlit as st
from rdflib import Graph, Namespace, RDF, RDFS
import pandas as pd


class RDFData:
    def __init__(self, namespaces, classes, properties):
        self.namespaces = namespaces
        self.classes = classes
        self.properties = properties

def load_file(file):

    # Create an RDF graph and load the data
    g = Graph()
    g.parse(file, format='turtle')

    # Get the namespaces used in the file
    namespaces = dict(g.namespaces())

    # Get the classes and properties used in the file
    classes = set(g.subjects(RDF.type, None))
    properties = set(g.predicates())

    # Print the number of classes in the file
    print('Number of classes:', len(classes))

    # Return an RDFData object with the namespaces, classes, and properties
    return RDFData(namespaces, classes, properties)


def compare_files(data1, data2):

    namespaces1 = data1.namespaces
    namespaces2 = data2.namespaces
    classes1 = data1.classes
    classes2 = data2.classes
    properties1 = data1.properties
    properties2 = data2.properties

    # Calculate the differences between the files
    common_namespaces = set(namespaces1.keys()).intersection(set(namespaces2.keys()))
    unique_namespaces1 = set(namespaces1.keys()).difference(set(namespaces2.keys()))
    unique_namespaces2 = set(namespaces2.keys()).difference(set(namespaces1.keys()))
    common_classes = classes1.intersection(classes2)
    unique_classes1 = classes1.difference(classes2)
    unique_classes2 = classes2.difference(classes1)
    common_properties = properties1.intersection(properties2)
    unique_properties1 = properties1.difference(properties2)
    unique_properties2 = properties2.difference(properties1)

     # Calculate the Jaccard similarity coefficient for the classes and properties
    class_similarity = len(classes1.intersection(classes2)) / len(classes1.union(classes2))
    property_similarity = len(properties1.intersection(properties2)) / len(properties1.union(properties2))

    # Calculate the overall similarity score as the average of the class and property similarity scores
    similarity_score = (class_similarity + property_similarity) / 2

    # Return the differences as a dictionary
    return {
        'common_namespaces': common_namespaces,
        'unique_namespaces1': unique_namespaces1,
        'unique_namespaces2': unique_namespaces2,
        'common_classes': common_classes,
        'unique_classes1': unique_classes1,
        'unique_classes2': unique_classes2,
        'common_properties': common_properties,
        'unique_properties1': unique_properties1,
        'unique_properties2': unique_properties2,
        'class_similarity': class_similarity,
        'property_similarity': property_similarity,
        'similarity_score': similarity_score
    }


# Allow the user to upload the catalogs as files
catalog_files = st.file_uploader('Upload DCAT data catalogs', type=['ttl'], accept_multiple_files=True)

# If files have been selected, load them and display a spinner while they are being loaded
if catalog_files and len(catalog_files) >= 2:
    with st.spinner('Loading files...'):
        file1 = catalog_files[0].read()
        file2 = catalog_files[1].read()
        data1 = load_file(file1)
        data2 = load_file(file2)
        differences = compare_files(data1, data2)
    st.success('Files loaded successfully!')


    # Display the differences as a table
    st.write('## Differences')
    st.write('### Namespaces')
    st.write('#### Common namespaces')
    st.write(pd.DataFrame({'Namespace': list(differences['common_namespaces'])}))
    st.write('#### Unique namespaces in file 1')
    st.write(pd.DataFrame({'Namespace': list(differences['unique_namespaces1'])}))
    st.write('#### Unique namespaces in file 2')
    st.write(pd.DataFrame({'Namespace': list(differences['unique_namespaces2'])}))
    st.write('### Classes')
    st.write('#### Common classes')
    st.write(pd.DataFrame({'Class': list(differences['common_classes'])}))
    st.write('#### Unique classes in file 1')
    st.write(pd.DataFrame({'Class': list(differences['unique_classes1'])}))
    st.write('#### Unique classes in file 2')
    st.write(pd.DataFrame({'Class': list(differences['unique_classes2'])}))
    st.write('### Properties')
    st.write('#### Common properties')
    st.write(pd.DataFrame({'Property': list(differences['common_properties'])}))
    st.write('#### Unique properties in file 1')
    st.write(pd.DataFrame({'Property': list(differences['unique_properties1'])}))
    st.write('#### Unique properties in file 2')
    st.write(pd.DataFrame({'Property': list(differences['unique_properties2'])}))
    st.write('### Similarity')
    st.write('#### Class similarity')
    st.write(differences['class_similarity'])
    st.write('#### Property similarity')
    st.write(differences['property_similarity'])
    st.write('#### Overall similarity score')
    st.write(differences['similarity_score'])

