# Remove duplicates without using set()
def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items
