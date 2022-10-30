#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    '''
    =========================
    BaseModel tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = 'BaseModel'

    def setUp(self):
        '''
        Setup
        '''
        pass

    def tearDown(self):
        '''
        Destroy Json File
        '''
        try:
            os.remove('JSONstorage.json')
        except Exception:
            pass

    def test_id(self):
        '''
        Attribute test
        '''
        base = self.test_class()
        self.assertIsInstance(base.id, str)

    def test_created_at(self):
        '''
        Attribute test
        '''
        base = self.test_class()
        now = datetime.now()
        self.assertIsInstance(base.created_at, datetime)
        self.assertTrue(now >= base.created_at)

    def test_updated_at(self):
        '''
        Attribute test
        '''
        base = self.test_class()
        base.updated_at = datetime.now()
        store = base.updated_at
        self.assertIsInstance(base.updated_at, datetime)
        base.updated_at = datetime.now()
        self.assertNotEqual(base.updated_at, store)

    def test_todict(self):
        '''
        to_dict test
        '''
        base = self.test_class()
        num = base.to_dict()
        self.assertEqual(base.to_dict(), num)

    def test_save(self):
        '''
        save Test
        '''
        self.assertFalse(os.path.exists('JSONstorage.json'))

    def test_str(self):
        '''
        str test
        '''
        base = self.test_class()
        _str = '[' + self.test_name + "] ({}) {}".format(
                              base.id, str(base.__dict__))
        self.assertEqual(str(base), _str)
