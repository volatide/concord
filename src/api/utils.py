from typing import Callable, TypeVar, Any, cast, get_type_hints, get_args, Dict, Type

T = TypeVar("T")


def map_types(meta: Callable[..., T], data: Any, _depth=0) -> T:
    # print("  "*_depth, meta, data)

    """
    Takes in an object and a dictionary from a json response and parses it using typedefs from the object into that object, recursively

    Example:
    ```py
    @dataclass
    class Bar:
        value: str
        another_value: list[int]

    @dataclass
    class Example:
        foo: Bar

    map_types(Example, {
        "foo": {
            "value": "Some text", 
            another_value: [1, 2, 3, 4]
        }
    })  #=> Example(foo=Foo(value="Some text", another_value=[1, 2, 3, 4]))
    ```
    """

    if type(data) == dict:
        if "errors" in data:
            raise RequestError(**data)

    # If the data is in it's base form, cast it to that (example, int, Snowflake)
    if type(data) not in [dict, list, tuple]:

        # A nullable field should not be cast to it's type (for example, str(None) #=> 'None')
        if data == None:
            return data
        return meta(data)

    # If the data is iterable (list or tuple),
    # map each item individually using list type args
    if type(data) in [list, tuple]:
        new = []
        for item in data:
            first = None
            types = get_args(meta)
            if not types:
                types = [meta]

            # This is due to Optional arguments (Union[T, None])
            for _type in types:
                try:
                    first = map_types(_type, item, _depth+1)
                    break
                except TypeError:
                    continue
            new.append(first)

        # This is to skip creating a nested function to allow lists to be mapped,
        # but is a bad way to do it
        return cast(T, new)

    # If the data is a dict, it should be mapped to it's meta (meta can be dict),
    # but should recurse as much as possible while there are typehints
    if type(data) == dict:
        new = {}
        hints: Dict[str, Type] = get_type_hints(meta)
        if not hints:
            return data
        for field, _type in hints.items():
            first = None
            if field not in data:
                continue
            types = get_args(_type)
            if not types:
                types = [_type]

            # This is due to Optional arguments (Union[T, None])
            for __type in types:
                try:
                    first = map_types(__type, data[field], _depth+1)
                    break
                except TypeError:
                    continue
            new[field] = first

        # Create object from own meta with named arguments
        return meta(**new)
    return meta(**data)


class RequestError(Exception):
    def __init__(self, code: int, message: str, errors: dict = {}, *args, **kwargs):
        self.code = code
        self.message = message
        self.errors = errors

        super().__init__(self.message)

    def __repr__(self):
        return f"RequestError(code={repr(self.code)},message={repr(self.message)},errors={repr(self.errors)}"
    
    __str__ = __repr__