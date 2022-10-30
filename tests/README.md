# Tests
![N|Solid](../images/unittest.jpeg)
# This directory contains all unit tests for this project.

# [BaseModel Tests](./test_models/test_base_model.py):

| Test                       		                               | Status|
| -----------------------------------------                    | ------|
| Model is an instance of `BaseModel`                          | `OK` :white_check_mark: |
| Model contains `id` attribute                                | `OK` :white_check_mark: |
| Model `id` attribute is a string                             | `OK` :white_check_mark: |
| Model instances have unique `id`                             | `OK` :white_check_mark: |
| Model contains `created_at` attribute                        | `OK` :white_check_mark: |
| Model `created_at` attribute is a datetime object            | `OK` :white_check_mark: |
| Model contains `updated_at` attribute                        | `OK` :white_check_mark: |
| Model `updated_at` attribute is a datetime object            | `OK` :white_check_mark: |
| Model `__str__` method prints the correct output             | `OK` :white_check_mark: |
| Model `save()` method changes the updated_at attribute       | `OK` :white_check_mark: |
| Model to_dict return object has `__class__` attribute        | `OK` :white_check_mark: |
| Model to_dict object `created_at` & `updated_at` are strings | `OK` :white_check_mark: |
| Model can be instantiated & reinstantiated with dict kwargs  | `OK` :white_check_mark: |
| Model instance attribute `created_at` is in ISO format       | `OK` :white_check_mark: |
| Model instance attribute `updated_at` is in ISO format       | `OK` :white_check_mark: |
