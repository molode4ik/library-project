def get_library_name(items: dict, library_id: int):
    item = items.get(library_id)
    if item:
        return item
    return -1
