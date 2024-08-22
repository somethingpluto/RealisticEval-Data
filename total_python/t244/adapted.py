import inspect


def method_arg_type_check(method_obj, *args, **kwargs):
    """
    Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
    expected data types, based on the method's signature.js. If there's a discrepancy, it raises a ValueError.

    Parameters:
        method_obj (Callable): The method for which arguments are checked.
        *args: Positional arguments passed to the method.
        **kwargs: Keyword arguments passed to the method.

    Optional argument:
        exclude (list of str): Names of parameters to exclude from the type check.
    """
    # Extract the list of parameters to exclude from the type check from kwargs, defaulting to an empty list if not provided
    exclude = kwargs.pop('exclude', [])
    exclude.append('self')  # Exclude 'self' by default since it refers to the method's instance

    # Get the signature.js of the method and prepare the expected types dictionary
    args_signature = inspect.signature(method_obj)
    bound_args = args_signature.bind(*args, **kwargs)
    bound_args.apply_defaults()

    expected_types = {
        param.name: param.annotation for param in args_signature.parameters.values()
        if param.name not in exclude and param.annotation is not inspect.Parameter.empty
    }

    # Check each argument against its expected type
    for arg_name, arg_type in expected_types.items():
        if arg_name in bound_args.arguments:
            actual_value = bound_args.arguments[arg_name]
            if not isinstance(actual_value, arg_type):
                passed_arg_type = type(actual_value).__name__
                expected_arg_type = arg_type.__name__
                raise ValueError(
                    f"{arg_name} should be of type {expected_arg_type}, but got type {passed_arg_type} instead.")