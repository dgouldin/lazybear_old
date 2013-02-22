def instance_is_dirty(instance, data, overwrite=False):
    """
    Returns ``True`` if the instance has attributes that are different
    from the values given in the data. Returns ``False`` otherwise.

    If ``overwrite`` is ``True``, the attributes of the instance are
    overwritten by the values given in the data.
    """
    dirty = False

    for k, v in data.items():
        if hasattr(instance, k) and getattr(instance, k) != v:
            dirty = True

            # Exit early if values are not being overwritten. Its
            # already known that the instance is dirty.
            if overwrite:
                setattr(instance, k, v)
            else:
                break

    return dirty

def update_or_create(manager, instance=None, force_save=True, **kwargs):
    if instance:
        obj = instance
        created = False
    else:
        obj, created = manager.get_or_create(**kwargs)
    if not created and 'defaults' in kwargs:
        dirty = instance_is_dirty(obj, kwargs['defaults'], True)
        if force_save or dirty:
            obj.save()
    return obj, created
