# Utilities to build context objects
class ContextUtils(object):

    @staticmethod
    def put_context(**kwargs):
        context = {};
        for arg_name in kwargs:
            context[arg_name] = kwargs[arg_name]
        return context
