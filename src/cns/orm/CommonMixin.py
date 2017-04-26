""" Behavioural Mixin for all ORM Objects.
"""


class CommonMixin(object):

    def __columns__(self):
        return self.__table__.columns._all_columns

    def __column_ignores__(self):
        """ Columns not to be considered by the Mixin """
        return []

    def __str__(self):
        cols    = self.__columns__()
        keyvals = {}
        ignores = self.__column_ignores__()

        for col in cols:
            if col.name not in ignores:
                val = getattr(self, col.name)
                keyvals[col.name] = val

        outstr  = "{name}({keyvals})".format(
            name    = self.__class__.__name__,
            keyvals = ", ".join(
                ["=".join((item[0], str(item[1]))) for item in keyvals.items()]
            )
        )

        return outstr
