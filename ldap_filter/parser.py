from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.item = elements[1]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.filt = elements[2]
        self.filtercomp = elements[2]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.filters = elements[2]
        self.filterlist = elements[2]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.filters = elements[2]
        self.filterlist = elements[2]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.filt = elements[2]
        self.filter = elements[2]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self.attr = elements[0]
        self.filtertype = elements[1]
        self.value = elements[2]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.attr = elements[0]
        self.equal = elements[1]
        self.wildcard_value = elements[2]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self.any = elements[1]


class TreeNode9(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode9, self).__init__(text, offset, elements)
        self.value = elements[0]


class TreeNode10(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode10, self).__init__(text, offset, elements)
        self.attr = elements[0]
        self.AttributeType = elements[0]
        self.opts = elements[1]


class TreeNode11(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode11, self).__init__(text, offset, elements)
        self.options = elements[1]


class TreeNode12(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode12, self).__init__(text, offset, elements)
        self.options = elements[1]


class TreeNode13(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode13, self).__init__(text, offset, elements)
        self.ALPHA = elements[0]


class TreeNode14(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode14, self).__init__(text, offset, elements)
        self.option = elements[0]
        self.options = elements[2]


class TreeNode15(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode15, self).__init__(text, offset, elements)
        self.ASCII_VALUE = elements[1]


class TreeNode16(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode16, self).__init__(text, offset, elements)
        self.HEX_CHAR = elements[1]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[^!*\\x29]')
    REGEX_2 = re.compile('^[a-fA-F0-9]')
    REGEX_3 = re.compile('^[\\x20]')
    REGEX_4 = re.compile('^[\\x09]')
    REGEX_5 = re.compile('^[0-9]')
    REGEX_6 = re.compile('^[a-zA-Z]')

    def _read_root(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['root'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_filter()
        if address0 is FAILURE:
            self._offset = index1
            index2, elements0 = self._offset, []
            address1 = FAILURE
            remaining0, index3, elements1, address2 = 0, self._offset, [], True
            while address2 is not FAILURE:
                address2 = self._read_FILL()
                if address2 is not FAILURE:
                    elements1.append(address2)
                    remaining0 -= 1
            if remaining0 <= 0:
                address1 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            else:
                address1 = FAILURE
            if address1 is not FAILURE:
                elements0.append(address1)
                address3 = FAILURE
                address3 = self._read_item()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
            if elements0 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode1(self._input[index2:self._offset], index2, elements0)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['root'][index0] = (address0, self._offset)
        return address0

    def _read_filter(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['filter'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            address2 = self._read_FILL()
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == '(':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'(\'')
            if address3 is not FAILURE:
                elements0.append(address3)
                address4 = FAILURE
                address4 = self._read_filtercomp()
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    chunk1 = None
                    if self._offset < self._input_size:
                        chunk1 = self._input[self._offset:self._offset + 1]
                    if chunk1 == ')':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\')\'')
                    if address5 is not FAILURE:
                        elements0.append(address5)
                        address6 = FAILURE
                        remaining1, index3, elements2, address7 = 0, self._offset, [], True
                        while address7 is not FAILURE:
                            address7 = self._read_FILL()
                            if address7 is not FAILURE:
                                elements2.append(address7)
                                remaining1 -= 1
                        if remaining1 <= 0:
                            address6 = TreeNode(self._input[index3:self._offset], index3, elements2)
                            self._offset = self._offset
                        else:
                            address6 = FAILURE
                        if address6 is not FAILURE:
                            elements0.append(address6)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_filter(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['filter'][index0] = (address0, self._offset)
        return address0

    def _read_filtercomp(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['filtercomp'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_and()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_or()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_not()
                if address0 is FAILURE:
                    self._offset = index1
                    address0 = self._read_item()
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['filtercomp'][index0] = (address0, self._offset)
        return address0

    def _read_and(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['and'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '&':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'&\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_FILL()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                address4 = self._read_filterlist()
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    remaining1, index3, elements2, address6 = 0, self._offset, [], True
                    while address6 is not FAILURE:
                        address6 = self._read_FILL()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            remaining1 -= 1
                    if remaining1 <= 0:
                        address5 = TreeNode(self._input[index3:self._offset], index3, elements2)
                        self._offset = self._offset
                    else:
                        address5 = FAILURE
                    if address5 is not FAILURE:
                        elements0.append(address5)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_and_filter(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['and'][index0] = (address0, self._offset)
        return address0

    def _read_or(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['or'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '|':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'|\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_FILL()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                address4 = self._read_filterlist()
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    remaining1, index3, elements2, address6 = 0, self._offset, [], True
                    while address6 is not FAILURE:
                        address6 = self._read_FILL()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            remaining1 -= 1
                    if remaining1 <= 0:
                        address5 = TreeNode(self._input[index3:self._offset], index3, elements2)
                        self._offset = self._offset
                    else:
                        address5 = FAILURE
                    if address5 is not FAILURE:
                        elements0.append(address5)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_or_filter(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['or'][index0] = (address0, self._offset)
        return address0

    def _read_not(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['not'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '!':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'!\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_FILL()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                address4 = self._read_filter()
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    remaining1, index3, elements2, address6 = 0, self._offset, [], True
                    while address6 is not FAILURE:
                        address6 = self._read_FILL()
                        if address6 is not FAILURE:
                            elements2.append(address6)
                            remaining1 -= 1
                    if remaining1 <= 0:
                        address5 = TreeNode(self._input[index3:self._offset], index3, elements2)
                        self._offset = self._offset
                    else:
                        address5 = FAILURE
                    if address5 is not FAILURE:
                        elements0.append(address5)
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_not_filter(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['not'][index0] = (address0, self._offset)
        return address0

    def _read_filterlist(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['filterlist'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_filter()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['filterlist'][index0] = (address0, self._offset)
        return address0

    def _read_item(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['item'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_wildcard()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_simple()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['item'][index0] = (address0, self._offset)
        return address0

    def _read_simple(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['simple'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_attr()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_filtertype()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_value()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_simple_filter(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['simple'][index0] = (address0, self._offset)
        return address0

    def _read_filtertype(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['filtertype'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_equal()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_approx()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_greater()
                if address0 is FAILURE:
                    self._offset = index1
                    address0 = self._read_less()
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['filtertype'][index0] = (address0, self._offset)
        return address0

    def _read_equal(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['equal'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '=':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'=\'')
        self._cache['equal'][index0] = (address0, self._offset)
        return address0

    def _read_approx(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['approx'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 2]
        if chunk0 == '~=':
            address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'~=\'')
        self._cache['approx'][index0] = (address0, self._offset)
        return address0

    def _read_greater(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['greater'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 2]
        if chunk0 == '>=':
            address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'>=\'')
        self._cache['greater'][index0] = (address0, self._offset)
        return address0

    def _read_less(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['less'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 2]
        if chunk0 == '<=':
            address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'<=\'')
        self._cache['less'][index0] = (address0, self._offset)
        return address0

    def _read_wildcard(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['wildcard'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_attr()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_equal()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_wildcard_value()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_wildcard(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['wildcard'][index0] = (address0, self._offset)
        return address0

    def _read_wildcard_value(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['wildcard_value'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        address1 = self._read_value()
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index2:index2], index2)
            self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_any()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index3 = self._offset
                address3 = self._read_value()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index3:index3], index3)
                    self._offset = index3
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode8(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['wildcard_value'][index0] = (address0, self._offset)
        return address0

    def _read_any(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['any'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '*':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'*\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                index3, elements2 = self._offset, []
                address4 = FAILURE
                address4 = self._read_value()
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    chunk1 = None
                    if self._offset < self._input_size:
                        chunk1 = self._input[self._offset:self._offset + 1]
                    if chunk1 == '*':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'*\'')
                    if address5 is not FAILURE:
                        elements2.append(address5)
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
                if elements2 is None:
                    address3 = FAILURE
                else:
                    address3 = TreeNode9(self._input[index3:self._offset], index3, elements2)
                    self._offset = self._offset
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_string(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['any'][index0] = (address0, self._offset)
        return address0

    def _read_attr(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['attr'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        address0 = self._read_AttributeDescription()
        self._cache['attr'][index0] = (address0, self._offset)
        return address0

    def _read_value(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['value'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_AttributeValue()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.return_string(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['value'][index0] = (address0, self._offset)
        return address0

    def _read_AttributeDescription(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttributeDescription'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_AttributeType()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index2 = self._offset
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == ';':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('";"')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                address4 = self._read_options()
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode11(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address2 is FAILURE:
                address2 = TreeNode(self._input[index2:index2], index2)
                self._offset = index2
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_options(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['AttributeDescription'][index0] = (address0, self._offset)
        return address0

    def _read_AttributeOptions(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttributeOptions'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == ';':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('";"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_options()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode12(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['AttributeOptions'][index0] = (address0, self._offset)
        return address0

    def _read_AttributeType(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttributeType'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_LDAP_OID()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_AttrTypeName()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['AttributeType'][index0] = (address0, self._offset)
        return address0

    def _read_AttrTypeName(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttrTypeName'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_ALPHA()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_AttrTypeChars()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_attr_type(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['AttrTypeName'][index0] = (address0, self._offset)
        return address0

    def _read_AttrTypeChars(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttrTypeChars'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_ALPHA()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_DIGIT()
            if address0 is FAILURE:
                self._offset = index1
                chunk0 = None
                if self._offset < self._input_size:
                    chunk0 = self._input[self._offset:self._offset + 1]
                if chunk0 == '-':
                    address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"-"')
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['AttrTypeChars'][index0] = (address0, self._offset)
        return address0

    def _read_LDAP_OID(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['LDAP_OID'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 1, self._offset, [], True
        while address2 is not FAILURE:
            address2 = self._read_DIGIT()
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            remaining1, index3, elements2, address4 = 0, self._offset, [], True
            while address4 is not FAILURE:
                index4, elements3 = self._offset, []
                address5 = FAILURE
                chunk0 = None
                if self._offset < self._input_size:
                    chunk0 = self._input[self._offset:self._offset + 1]
                if chunk0 == '.':
                    address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"."')
                if address5 is not FAILURE:
                    elements3.append(address5)
                    address6 = FAILURE
                    remaining2, index5, elements4, address7 = 1, self._offset, [], True
                    while address7 is not FAILURE:
                        address7 = self._read_DIGIT()
                        if address7 is not FAILURE:
                            elements4.append(address7)
                            remaining2 -= 1
                    if remaining2 <= 0:
                        address6 = TreeNode(self._input[index5:self._offset], index5, elements4)
                        self._offset = self._offset
                    else:
                        address6 = FAILURE
                    if address6 is not FAILURE:
                        elements3.append(address6)
                    else:
                        elements3 = None
                        self._offset = index4
                else:
                    elements3 = None
                    self._offset = index4
                if elements3 is None:
                    address4 = FAILURE
                else:
                    address4 = TreeNode(self._input[index4:self._offset], index4, elements3)
                    self._offset = self._offset
                if address4 is not FAILURE:
                    elements2.append(address4)
                    remaining1 -= 1
            if remaining1 <= 0:
                address3 = TreeNode(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            else:
                address3 = FAILURE
            if address3 is not FAILURE:
                elements0.append(address3)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_oid_type(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['LDAP_OID'][index0] = (address0, self._offset)
        return address0

    def _read_options(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['options'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_option()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == ';':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('";"')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_options()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_string(self._input, index2, self._offset, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_option()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['options'][index0] = (address0, self._offset)
        return address0

    def _read_option(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['option'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_AttrTypeChars()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.return_string(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['option'][index0] = (address0, self._offset)
        return address0

    def _read_AttributeValue(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AttributeValue'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_EscapedCharacter()
        if address0 is FAILURE:
            self._offset = index1
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[^!*\\x29]')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['AttributeValue'][index0] = (address0, self._offset)
        return address0

    def _read_EscapedCharacter(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['EscapedCharacter'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '\\':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'\\\\\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_ASCII_VALUE()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_escaped_char(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['EscapedCharacter'][index0] = (address0, self._offset)
        return address0

    def _read_ASCII_VALUE(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['ASCII_VALUE'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_HEX_CHAR()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_HEX_CHAR()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.return_hex(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['ASCII_VALUE'][index0] = (address0, self._offset)
        return address0

    def _read_HEX_CHAR(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['HEX_CHAR'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_2.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[a-fA-F0-9]')
        self._cache['HEX_CHAR'][index0] = (address0, self._offset)
        return address0

    def _read_FILL(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['FILL'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_SPACE()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_TAB()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_SEP()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['FILL'][index0] = (address0, self._offset)
        return address0

    def _read_SPACE(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SPACE'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[\\x20]')
        self._cache['SPACE'][index0] = (address0, self._offset)
        return address0

    def _read_TAB(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['TAB'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_4.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[\\x09]')
        self._cache['TAB'][index0] = (address0, self._offset)
        return address0

    def _read_DIGIT(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['DIGIT'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_5.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[0-9]')
        self._cache['DIGIT'][index0] = (address0, self._offset)
        return address0

    def _read_ALPHA(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['ALPHA'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_6.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[a-zA-Z]')
        self._cache['ALPHA'][index0] = (address0, self._offset)
        return address0

    def _read_SEP(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SEP'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 2]
        if chunk0 == '\r\n':
            address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\r\\n"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '\n':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\n"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['SEP'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_root()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()