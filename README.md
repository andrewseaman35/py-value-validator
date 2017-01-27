# py_value_validator

This is a Python module that provides an easy way to validate values. 
The base class provides some generic comparisons and should
be overridden in order to define comparisons for other classes. 

## Installation

Install using pip
```bash
$ pip install py-value-validator
```

## Usage

By overriding the functions class, validation functions can be added by data type
or to the generic function list. Any function that is specified as generic may be
used by any data of any type being validated.
```python
from py_value_validator.value_validator import GenericValidatorFunctions

class ValidatorFunctions(GenericValidatorFunctions):
    def _add_typed_functions(self):
        self._add_function(str, "contains", contains)
        self._add_function("generic", "is_not_none", is_not_none)

def contains(mine, yours):
    return yours in mine

def is_not_none(mine, yours=None):
    return mine is not None
```

Create a validator with an instance of the function class.
```python
from py_value_validator.value_validator import ValueValidator

_validator_functions = ValidatorFunctions()
validator = ValueValidator(_validator_functions)
```

Define a list of tuples that define the validation for the given value.
```python
validations = [('contains', 'ell'), ('is_not_none', None)]
```

Run the validations against a value and keep an eye out for a ValidationError.
```python
try:
    validator.validate("hello, world!", validations)
except ValidationError as validation_error:
    print("Value did not pass validation!")
```
