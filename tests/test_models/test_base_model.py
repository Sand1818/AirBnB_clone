#!/usr/bin/python3
"""BaseModel class unnit test"""

import models
from models.base_model import BaseModel
import datetime
import unittest
import uuid


class test_for_basemodel(unittest.TestCase):
    """BaseModel test"""

    def test_id(self):
        """test id"""
        ubm1 = BaseModel()
        ubm2 = BaseModel()
        self.assertTrue(isinstance(ubm1, BaseModel))
        self.assertNotEqual(ubm1.id, ubm2.id)
        ubm1.name = "san_acca"
        self.assertEqual(ubm1.name, "san_acca")
        self.assertTrue(isinstance(ubm1.name, str))
        ubm1.age = 5
        self.assertEqual(ubm1.age, 5)
        self.assertTrue(isinstance(ubm1.age, int))
        self.assertTrue(isinstance(ubm1.created_at, datetime.datetime))
        self.assertTrue(isinstance(ubm1.updated_at, datetime.datetime))
        self.assertTrue(isinstance(ubm1.id, str))
        self.assertTrue(isinstance(ubm1.to_dict(), dict))
        self.assertTrue(hasattr(ubm1, 'id'))
        self.assertTrue(hasattr(ubm1, 'created_at'))
        self.assertTrue(hasattr(ubm1, 'updated_at'))
        self.assertTrue(hasattr(ubm1, 'age'))
        self.assertTrue(hasattr(ubm1, 'name'))
        self.assertTrue(hasattr(eval(ubm1.__class__.__name__), '__str__'))
        dic = ubm1.to_dict()
        self.assertTrue(hasattr(dic, '__class__'))

        self.assertTrue(hasattr(ubm1, 'to_dict'))
        self.assertTrue(hasattr(ubm1, '__str__'))

        self.assertTrue(callable(type(ubm1.to_dict())))
        self.assertTrue(callable(type(ubm1.__str__())))

        s0 = str(ubm1)
        self.assertMultiLineEqual(ubm1.__str__(), str(ubm1))

        my_dict = {}
        for k, v in ubm1.__dict__.items():
            if k == 'created_at':
                my_dict[k] = v.isoformat()
            elif k == 'updated_at':
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
            my_dict['__class__'] = ubm1.__class__.__name__

        self.assertDictEqual(ubm1.to_dict(), my_dict)

        d1 = ubm1.updated_at
        ubm1.save()
        objs = unique_models.storage.all()
        key = 'BaseModel' + '.' + ubm1.id
        if key in objs:
            r = objs[key].to_dict()
            for k, v in r.items():
                self.assertEqual(r[k], ubm1.to_dict()[k])
        d2 = ubm1.updated_at
        self.assertNotEqual(d1, d2)

        sj_mod = BaseModel()
        sj_mod.name = "san_acca"
        sj_mod.my_number = 89
        sj_mod_json = sj_mod.to_dict()
        for key in sj_mod_json.keys():
            self.assertTrue(
                hasattr(sj_mod, key))
