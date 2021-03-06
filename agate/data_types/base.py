#!/usr/bin/env python

#: Default values which will be automatically cast to :code:`None`
DEFAULT_NULL_VALUES = ('', 'na', 'n/a', 'none', 'null', '.')

class DataType(object): #pragma: no cover
    """
    Base class for data types.

    :param null_values: A sequence of values which should be cast to
        :code:`None` when encountered with this type.
    """
    def __init__(self, null_values=DEFAULT_NULL_VALUES):
        self.null_values = null_values

    def test(self, d):
        """
        Test, for purposes of type inference, if a value could possibly be valid
        for this column type. This will work with values that are native types
        and values that have been stringified.
        """
        raise NotImplementedError

    def cast(self, d):
        """
        Coerce a given string value into this column's data type.
        """
        raise NotImplementedError
