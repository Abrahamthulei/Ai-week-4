# Manual version
def sort_dicts(data, key):
    """Sorts a list of dictionaries by a given key"""
    return sorted(data, key=lambda x: x[key])

# Copilot AI-suggested version
def sort_dicts_by_key(dict_list, sort_key):
    """Sorts a list of dictionaries using .get() to avoid KeyError"""
    return sorted(dict_list, key=lambda item: item.get(sort_key, ''))
