def find_key(obj: dict | list[dict], key: str) -> list:
    """
    Find all values of a given key within a nested dict or list of dicts

    @param obj: dictionary or list of dictionaries
    @param key: key to search for
    @return: list of values
    """
    def helper(obj: any, key: str, L: list) -> list:
        if not obj:
            return L

        if isinstance(obj, list):
            for e in obj:
                L.extend(helper(e, key, []))
            return L

        if isinstance(obj, dict) and obj.get(key):
            L.append(obj[key])

        if isinstance(obj, dict) and obj:
            for k in obj:
                L.extend(helper(obj[k], key, []))
        return L

    return helper(obj, key, [])