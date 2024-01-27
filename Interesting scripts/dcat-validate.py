import rdflib
import unicodedata
from isodate import ISO8601Error

def validate_date(date_str):
    try:
        rdflib.term.Literal(date_str, datatype=rdflib.XSD.date)
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    except ISO8601Error as iso_err:
        print(f"ISO8601Error: {iso_err}")
        return False

def check_turtle_well_formedness(file_path):
    try:
        g = rdflib.Graph()
        g.parse(file_path, format="ttl")
        return True
    except Exception as e:
        print(f"Error parsing TTL file: {e}")
        return False

def validate_text_encoding(text):
    try:
        unicodedata.normalize("NFKD", text)
        return True
    except UnicodeError:
        return False

def main():
    file_path = "d1.ttl"

    # 1. Data Format Validation - Check for valid dates
    date_literal = "23"  # Example date with unrecognized format
    is_valid_date = validate_date(date_literal)
    print(f"Date Literal Validation: {is_valid_date}")

    # 2. Turtle (TTL) Well-Formedness
    is_turtle_well_formed = check_turtle_well_formedness(file_path)
    print(f"Turtle Well-Formedness: {is_turtle_well_formed}")

    # 3. Encoding Check - Example text
    example_text = "Some text encoded using strange symbols: äëìøü"
    is_encoding_valid = validate_text_encoding(example_text)
    print(f"Text Encoding Validation: {is_encoding_valid}")


    from datetime import datetime
import re


if __name__ == "__main__":
    main()
