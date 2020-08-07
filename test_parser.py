import unittest
import parser
from unittest import mock


class TestFromCommandMessageToList(unittest.TestCase):

    def test_success(self):
        command = "command"
        item_1 = "item_1"
        item_2 = "item_2"
        item_3 = "item_3"
        separator = ".."
        message = " " + item_1 + " " + separator + " " + item_2 + " " + separator + " " + item_3
        input_data = "/" + command + message
        items = [item_1, item_2, item_3]

        parser.cut_off_command = mock.MagicMock()
        parser.cut_off_command.return_value = command, message

        result_command, result_items = parser.from_command_message_to_list(input_data)

        self.assertEqual(command, result_command)
        self.assertEqual(items, result_items)

    def test_another_separator_success(self):
        command = "command"
        item_1 = "item_1"
        item_2 = "item_2"
        item_3 = "item_3"
        separator = "///"
        message = " " + item_1 + " " + separator + " " + item_2 + " " + separator + " " + item_3
        input_data = "/" + command + message
        items = [item_1, item_2, item_3]

        parser.cut_off_command = mock.MagicMock()
        parser.cut_off_command.return_value = command, message

        result_command, result_items = parser.from_command_message_to_list(input_data, separator)

        self.assertEqual(command, result_command)
        self.assertEqual(items, result_items)


class TestCutOffCommand(unittest.TestCase):

    def test_success(self):
        command = "command"
        rest = "some text, bla-bla-bla"
        command_message = "/" + command + " " + rest

        result_command, result_rest = parser.cut_off_command(command_message)

        self.assertEqual(command, result_command)
        self.assertEqual(rest, result_rest)
