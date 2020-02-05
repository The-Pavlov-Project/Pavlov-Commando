
def has_permission(func, command=None, permissions=0):

    def inner(*args, **kwargs):
        print("before Execution")
        command_descriptor, module, class_name = command
        if command_descriptor.permissions >= permissions:
            returned_value = func(*args, **kwargs)
        else:
            returned_value = ''

        print("after Execution")
        return returned_value

    return inner
