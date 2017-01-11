import sys
import functools

from value_validator import (ValueValidator, ValidationError, GenericValidatorFunctions)


class ValidatorFunctions(GenericValidatorFunctions):
    def add_typed_functions(self):
        self._add_function(str, "contains", contains)
        self._add_function(int, "contains", int_contains)
        self._add_function("generic", "is_not_none", is_not_none)

def int_contains(mine, yours):
    return str(yours) in str(mine)

def contains(mine, yours):
    return yours in mine

def is_not_none(mine, yours=None):
    return mine is not None

def main():
    validator_functions = ValidatorFunctions()
    validator = ValueValidator(validator_functions)

    success_validations = [("contains", "ell"), ("is_not_none", None)]
    try:
        validator.validate("Hello, world!", success_validations)
    except ValidationError as validation_error:
        print("Value did not pass validation!")
        print(validation_error)

    failed_validations = [("contains", "ell"), ("contains", "123")]
    try:
        validator.validate("Hello, world!", failed_validations)
    except ValidationError as validation_error:
        print("Value did not pass validation!")
        print(validation_error)

    int_validations =[("contains", 4), ("less_than", 11)]
    try:
        validator.validate(14, int_validations)
    except ValidationError as validation_error:
        print("Value did not pass validation!")
        print(validation_error)


if __name__ == "__main__":
    sys.exit(main())