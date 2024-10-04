def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if not cls in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton