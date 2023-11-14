def LockedClass(first_name):
    def set_first_name(instance, value):
        nonlocal first_name
        first_name = value

    def get_first_name(instance):
        return first_name

    def set_attr(instance, name, value):
        if name == "first_name":
            set_first_name(instance, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")

    def get_attr(instance, name):
        if name == "first_name":
            return get_first_name(instance)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")

    return set_attr, get_attr
