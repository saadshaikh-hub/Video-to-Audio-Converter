# Utility functions for Video to Audio Converter
# Developed by: Saad Shaikh
# Academic Details: BSc Computer Science, University Of Mumbai, 2022

import os

def validate_file_path(file_path):
    """
    Validates if the given file path exists.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)
