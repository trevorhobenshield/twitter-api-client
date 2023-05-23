class Singleton(object):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class SubclassesMixin:
    @classmethod
    def _get_all_subclasses(cls):
        all_subclasses = []
        for subclass in cls.__subclasses__():
            all_subclasses.append(subclass)
            all_subclasses.extend(subclass._get_all_subclasses())

        return all_subclasses

    @classmethod
    def _get_subclasses_with(cls, attribute):
        return [x for x in cls._get_all_subclasses() if hasattr(x, attribute)]

    @classmethod
    def _get_subclasses_dict(cls, attribute):
        return dict(
            [
                (getattr(x, attribute), x)
                for x in cls._get_all_subclasses()
                if hasattr(x, attribute)
            ]
        )