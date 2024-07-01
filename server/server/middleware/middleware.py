def pipe(req, res, *args):
    if len(args) == 0:
        raise Exception("Invalid number of arguments passed to function flow")
    def flow(args, args_left):
        if args_left == 1:
            return lambda : args[-1](req, res)
        return lambda : args[-args_left](req, res, flow(args, args_left - 1))
    return flow(args, len(args))()
