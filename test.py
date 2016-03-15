import unittest
import test_data
from PrintProxy import switch_quad_words, format_url, url_to_file

class TestSwitchQuadWords(unittest.TestCase):
    def test_switch(self):
        result = switch_quad_words(test_data.WEB_MAP_JSON)
        self.assertEqual(result, test_data.WEB_MAP_JSON_SWITCHED)

    def test_return_original_if_no_quad_word(self):
        value = 'blah'
        self.assertEqual(switch_quad_words(value), value)


class TestFormatURL(unittest.TestCase):
    def test_adds_protocal(self):
        result = format_url(r'test/blah')
        self.assertEqual(result, r'http://test/blah/execute')
    def test_no_duplicate_protocal(self):
        result = format_url(r'http://test/blah')
        self.assertEqual(result, r'http://test/blah/execute')


class TestURLToFile(unittest.TestCase):
    def test_convert_url_to_file_path(self):
        self.assertEqual(url_to_file(test_data.FILE_URL), test_data.FILE_PATH)
