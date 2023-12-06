"""
The flatten function is defined in this module.
This function is used in order to flatten the keys of a nested dictionary.
"""
from collections.abc import MutableMapping


def flatten(dictionary, parent_key='', separator='__'):
    """
    This function takes a nested dictionary and flattens all of the keys.
    Args:
        dictionary: the dictionary that will be flattened
        parent_key: key that is used to identify the nested json
        separator: the separator that will be used to connect the nested keys
    Returns:
        A flattened dictionary
    """
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)
