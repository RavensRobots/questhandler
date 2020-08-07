import re


def from_command_message_to_list(command_message, separator=".."):
    """return the command without '/' and a list of items"""
    command, message = cut_off_command(command_message)
    items = message.split(separator)
    result_items = list()
    for i in items:
        result_items.append(i.strip())
    return command, result_items


def cut_off_command(command_message):
    """return command without '/' and the rest message"""
    result = re.match(r"/(\w+) (.*)", command_message)
    return result.group(1), result.group(2)
