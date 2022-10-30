#!/usr/bin/python3
"""unittests for BaseClass from which all major objects inherits"""

from datetime import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel_Instantiation(unittest.TestCase):
    """Tests for BaseModel instantiation"""

    def test_IsInstanceOf(self):
        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)

    def test_ContainsId(self):
        model1 = BaseModel()
        self.assertTrue(hasattr(model1, "id"))

    def test_IdType(self):
        model1 = BaseModel()
        self.assertEqual(type(model1.id), str)

    def test_CompareTwoInstancesId(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_ContainsCreated_at(self):
        model1 = BaseModel()
        self.assertTrue(hasattr(model1, "created_at"))

    def test_Created_atInstance(self):
        model1 = BaseModel()
        self.assertIsInstance(model1.created_at, datetime)

    def test_ContainUpdated_at(self):
        model1 = BaseModel()
        self.assertTrue(hasattr(model1, "updated_at"))

    def test_Updated_atInstance(self):
        model1 = BaseModel()
        self.assertIsInstance(model1.updated_at, datetime)

class TestBaseModel_Instance_Print(unittest.TestCase):
    """This class tests the return value of BaseModel's __str__ method."""

    def test_str_value(self):
        model1 = BaseModel()
        model_str = "[{}] ({}) {}".format("BaseModel", model1.id, str(model1.__dict__))
        self.assertEqual(str(model1), model_str)

class TestBaseModel_Save_Method(unittest.TestCase):
    """This class tests BaseModel's save method"""

    def test_validates_save(self):
        model1 = BaseModel()
        updated_at_1 = model1.updated_at
        model1.save()
        updated_at_2 = model1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """This class tests BaseModel's to_dict method."""

    def test_className_present(self):
        model1 = BaseModel()
        model_dict = model1.to_dict()
        self.assertTrue(hasattr(model_dict, "__class__"))
    
    def test_formatted_attributes(self):
        model1 = BaseModel()
        model_dict = model1.to_dict()
        self.assertEqual(type(model_dict["created_at"]), str)
        self.assertEqual(type(model_dict["updated_at"]), str)

class TestBaseModel_Kwargs_Instance(unittest.TestCase):
    """This class tests BaseModel instantiation with keyword arguments"""

    def test_reinstantiation_from_dict(self):
        model1 = BaseModel()
        model1.my_number = 89

        kwargs_dict = model1.to_dict()
        model2 = BaseModel(**kwargs_dict)
        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.my_number, model2.my_number)
        self.assertEqual(model1.created_at, model2.created_at.isoformat())
        self.assertEqual(model1.updated_at, model2.updated_at.isoformat())
        
if __name__ == "__main__":
    unittest.main()
