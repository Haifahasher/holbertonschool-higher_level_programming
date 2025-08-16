#!/usr/bin/env python3
"""
XML Serialization Module

This module provides functionality to serialize Python dictionaries to XML format
and deserialize XML files back to Python dictionaries.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to

    Returns:
        None
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Iterate through dictionary items and add them as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception as e:
        print(f"Error serializing dictionary to XML: {e}")


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back to a Python dictionary.

    Args:
        filename (str): The filename to read the XML data from

    Returns:
        dict: The deserialized Python dictionary, or None if an error occurs
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from XML elements
        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML file '{filename}': {e}")
        return None
    except Exception as e:
        print(f"Error deserializing XML: {e}")
        return None
