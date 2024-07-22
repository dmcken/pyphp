'''Tests for pyphp module'''
import pyphp

def test_http_build_query_double():
    """Test single layer.
    """
    double_level_dict = {
        'main_attributes': {'mac': '123456789ABC'}
    }
    actual = pyphp.http_build_query(double_level_dict)
    expected = 'main_attributes%5Bmac%5D=123456789ABC'
    assert actual == expected, "Double level dictionary query string incorrect"
