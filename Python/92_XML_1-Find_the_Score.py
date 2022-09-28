def get_attr_number(node):
    res = 0
    for child in node.iter():
        res += len(child.attrib)
    return res
