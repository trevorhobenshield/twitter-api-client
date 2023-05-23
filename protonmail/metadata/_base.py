from abc import ABCMeta, abstractmethod
from ..utils import SubclassesMixin


class MetadataBackend(SubclassesMixin, metaclass=ABCMeta):

    @classmethod
    def get_backend(cls, metadata_backend="default"):
        subclasses_dict = cls._get_subclasses_dict("metadata_backend")
        if metadata_backend not in subclasses_dict:
            raise NotImplementedError(
                "API Metadata Backend not implemented"
            )

        return subclasses_dict[metadata_backend]()

    @staticmethod
    @abstractmethod
    def store_alternative_route():
        """Store alternative route.

        This should store the url and also the time when it was stored.
        """
        pass

    @staticmethod
    @abstractmethod
    def try_original_url():
        """Determine if next api call should use the original URL or not."""
        pass

    @staticmethod
    @abstractmethod
    def get_alternative_url():
        """Get stored URL."""
        pass

    @property
    @abstractmethod
    def cache_dir_path():
        """Getter for cache directory path."""
        pass

    @cache_dir_path.setter
    @abstractmethod
    def cache_dir_path():
        """Setter for cache directory path."""
        pass
