import unittest
import manager


class TestQuestListToDict(unittest.TestCase):

    def test_all_fields_success(self):
        name = "name"
        description = "description"
        urgency = 2
        value = 1
        interval = 24
        step = "hour"
        quest_list = ["name", "description", "item_3", ]