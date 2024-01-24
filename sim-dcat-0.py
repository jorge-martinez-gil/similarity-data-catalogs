# This code snippet is used to test the similarity between two Data Catalogs

import difflib

entry1 = '''ex:dataset-002
  a dcat:Dataset ;
  dcterms:title "Imaginaaaaaaaaary dataset"@en ;
  dcterms:title "Conjunto de datos imaginario"@es ;
  dcat:keyword "accountability"@en, "transparency"@en, "payments"@en ;
  dcat:keyword "responsabilidad"@es, "transparencia"@es, "pagos"@es ;
  dcterms:creator ex:finance-employee-001 ;
  dcterms:issued "2011-12-05"^^xsd:date ;
  dcterms:modified "2011-12-15"^^xsd:date ;
  dcat:contactPoint <http://dcat.example.org/transparency-office/contact> ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2011-07-01"^^xsd:date ; 
    dcat:endDate   "2011-09-30"^^xsd:date ;
  ];
  dcat:temporalResolution "P1D"^^xsd:duration ;
  dcterms:spatial <http://sws.geonames.org/6695072/> ;
  dcat:spatialResolutionInMeters "110.0"^^xsd:decimal ;
  dcterms:publisher ex:finance-ministry ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;
  dcterms:accrualPeriodicity <http://purl.org/linked-data/sdmx/2009/code#freq-W>  ;
  dcat:distribution ex:dataset-004-csv ;
  dcat:distribution ex:dataset-002-ttl ;
  .'''

entry2 = '''ex:dataset-003
  a dcat:Dataset ;
  dcterms:title "Imaginaryeeeeeee dataset"@en ;
  dcterms:title "Conjunto de datoseeeeee imaginario"@es ;
  dcat:keyword "accountabieeeeeelity"@en, "transparency"@en, "payments"@en ;
  dcat:keyword "responsabilidad"@es, "transparencia"@es, "pagos"@es ;
  dcterms:creator ex:finaneeeeeece-employee-001 ;
  dcterms:issued "2011-12-05"^^xsd:date ;
  dcterms:modified "2011-12-15"^^xsd:date ;
  dcat:contactPoint <http://dcat.example.org/transparency-office/contact> ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2011-07-01"^^xsd:date ; 
    dcat:endDate   "2011-09-30"^^xsd:date ;
  ];
  dcat:temporalResolution "P1D"^^xsd:duration ;
  dcterms:spatial <http://sws.geonames.org/6695072/> ;
  dcat:spatialResolutionInMeters "30.0"^^xsd:decimal ;
  dcterms:publisher ex:finance-ministry ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;
  dcterms:accrualPeriodicity <http://purl.org/linked-data/sdmx/2009/code#freq-W>  ;
  dcat:distribution ex:dataset-003-csv ;
  dcat:distribution ex:dataset-003-ttl ;
  .'''

# Calculate the similarity ratio between the two entries
similarity_ratio = difflib.SequenceMatcher(None, entry1, entry2).ratio()

print(f"The similarity ratio between the two entries is {similarity_ratio}")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the texts to compare
text1 = '''
ex:dataset-001
  a dcat:Dataset ;
  dcterms:title "Machine parameters"@en ;
  dcterms:title "Parametros de la maquina"@es ;
  dcat:keyword "accountability"@en, "transparency"@en;
  dcat:keyword "responsabilidad"@es, "transparencia"@es;
  dcterms:creator ex:alejandro-espert ;
  dcterms:issued "2022-10-05"^^xsd:date ;
  dcterms:modified "2022-10-15"^^xsd:date ;
  dcat:contactPoint <https://www.teaming-ai.eu/somebody/contact> ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2022-07-01"^^xsd:date ; 
    dcat:endDate   "2022-09-30"^^xsd:date ;
  ];
  dcat:temporalResolution "P1D"^^xsd:duration ;
  dcterms:spatial <http://sws.geonames.org/6695072/> ;
  dcat:spatialResolutionInMeters "1.0"^^xsd:decimal ;
  dcterms:publisher ex:industrias-alegre ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;
  dcterms:accrualPeriodicity <http://purl.org/linked-data/sdmx/2009/code#freq-W>  ;
  dcat:distribution ex:dataset-001-csv ;
  dcat:distribution ex:dataset-001-ttl ;
'''

text2 = '''
ex:dataset-002
  a dcat:Dataset ;
  dcterms:title "Imaginary dataset"@en ;
  dcterms:title "Conjunto de datos imaginario"@es ;
  dcat:keyword "accountability"@en, "transparency"@en, "payments"@en ;
  dcat:keyword "responsabilidad"@es, "transparencia"@es, "pagos"@es ;
  dcterms:creator ex:finance-employee-001 ;
  dcterms:issued "2011-12-05"^^xsd:date ;
  dcterms:modified "2011-12-15"^^xsd:date ;
  dcat:contactPoint <http://dcat.example.org/transparency-office/contact> ;
  dcterms:temporal [ a dcterms:PeriodOfTime ;
    dcat:startDate "2011-07-01"^^xsd:date ; 
    dcat:endDate   "2011-09-30"^^xsd:date ;
  ];
  dcat:temporalResolution "P1D"^^xsd:duration ;
  dcterms:spatial <http://sws.geonames.org/6695072/> ;
  dcat:spatialResolutionInMeters "30.0"^^xsd:decimal ;
  dcterms:publisher ex:finance-ministry ;
  dcterms:language <http://id.loc.gov/vocabulary/iso639-1/en> ;
  dcterms:accrualPeriodicity <http://purl.org/linked-data/sdmx/2009/code#freq-W>  ;
  dcat:distribution ex:dataset-002-csv ;
  dcat:distribution ex:dataset-002-ttl ;
'''

# Define the vectorizer and compute the tf-idf matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

# Compute the cosine similarity between the two texts
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

print(f"The cosine similarity between the two texts is: {cosine_sim}")
