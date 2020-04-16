def _decor_output_dec(func):
    def wrapper(inp_str):
        print('=' * len(inp_str))
        func(inp_str)
        print('=' * len(inp_str))
    return wrapper


@_decor_output_dec
def decor_output(in_str):
    print(in_str)