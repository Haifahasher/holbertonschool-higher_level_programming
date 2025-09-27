#!/usr/bin/env python3
"""
Simple templating program that generates personalized invitation files
from a template with placeholders and a list of objects.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs errors
    """
    # Check input types
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return
    
    if not isinstance(attendees, list):
        logging.error("Attendees must be a list of dictionaries")
        return
    
    # Check if template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            logging.error(f"Attendee at index {i-1} is not a dictionary, skipping.")
            continue
        
        # Create a copy of the template for this attendee
        personalized_template = template
        
        # Replace placeholders with values, using "N/A" for missing data
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            personalized_template = personalized_template.replace(f"{{{placeholder}}}", str(value))
        
        # Write to output file
        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(personalized_template)
            logging.info(f"Generated {output_filename}")
        except Exception as e:
            logging.error(f"Error writing {output_filename}: {e}")


if __name__ == "__main__":
    # Example usage
    template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
    
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    
    generate_invitations(template, attendees)
