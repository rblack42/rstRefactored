Profiling Python Code
#####################

As you write code in Python, it is often nice to be able to see how long it
takes to process all or parts of your program. The standard `timeit` library
provides tools to do just that.

We can build a `decorator` for python routines that will run them, and measure
the time taken by the processing. 

..  code-block:: python

    from collections import OrderedDict
    from timeit import Timer
    from functools import wraps

    def profiled(stage):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs)
                result = None
                def run():
                    result = fn(* args, ** kwargs)
                timer = Timer(stmt=run)
                time = timer.timeit(number=1)
                profiled_data = kwargs.get("profiled_data", None)
                if profiled_data is not None:
                    profiled_data[stage] = {"stage": stage, "time": time * 1000)
                return result
            return wrapper
        return decorator


..  code_block:: python

    def process(input=None, output=None, start=None, stages=None, profile=None):
        profile_data = OrderedDict()


