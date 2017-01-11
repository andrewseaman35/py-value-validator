# py-value-validator

This is a Python module that provides an easy way to validate values in
other projects. The base class provides some generic comparisons and should
be overridden in order to define comparisons for other classes. 

## Installation

Add the source as a submodule to your project
```
$ git submodule add https://github.com/andrewseaman35/py-value-validator.git
```

## Usage

By overriding the functions class, validation functions can be added by 
data type or to the generic function list. Custom functions can
also be added by using partials.
```
import functools

class ValidatorFunctions(GenericValidatorFunctions):
    def _add_typed_functions(self):
        self._functions[str] = {
            'contains': self._value.contains, # set type function
            'has_letter_e': functools.partial(has_letter_e, self._value) # set custom function with partials
        }
        self._functions['generic']['not_equals'] = self._value.__ne__ # add generic functions

def has_letter_a(value):
    return "e" in value
```

Create a validator with the function class.
```
validator = ValueValidator(ValidatorFunctions)
```

Define a list of tuples that define the validation for the given value.
```
validations = [('contains', 'ell'), ('has_letter_e', None)]
```

Run the validations against a value and keep an eye out for a ValidationError
```
try:
    validator.validate("hello, world!", validations)
except ValidationError as validation_error:
    print(validation_error)
```
