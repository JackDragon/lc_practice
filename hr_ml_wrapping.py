def check_wrapper():
    @wrapper
    def fun1(x):
        return x + 1

    print(fun1(1))
    # The function returned: 2

    @wrapper
    def fun2():
        return {'a': 1, 'b': [2, 3], 'cde': 4}

    print(fun2())
    # The function returned: {... 'edc': 4 ...}
# Enter your code here. It should implement @wrapper.
def wrapper(function):
    def reverse_if_string(key):
        if isinstance(key, str):
            return key[::-1]
        else:
            return key
    def wrap(*args, **kwargs):
        ret_val = function(*args, **kwargs)
        if isinstance(ret_val, dict):
            # not going to change the dict in place because we might have 'cde' and 'edc' as keys and we wouldn't want to overwrite
            return "The function returned: {}".format({reverse_if_string(key):ret_val[key] for key in ret_val.keys()})
        else:
            return "The function returned: {}".format(ret_val)
    return wrap
check_wrapper()