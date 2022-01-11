import abc


class DictUtils(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse_response(self, response):
        """ Define behavior in child class """
        raise NotImplementedError

    @abc.abstractmethod
    def get_definitions(self):
        """ Define behavior in child class """
        raise NotImplementedError
