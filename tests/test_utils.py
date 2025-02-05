from unittest.mock import mock_open, patch

from src.utils import create_object_from_data, read_json


@patch("os.path.abspath", return_value="fake_path")
@patch("builtins.open", new_callable=mock_open, read_data='{"test": "test"}')
def test_read_json(mock_open, mock_os):
    """ Тест функции чтения данных """
    result = read_json("fakefile")
    mock_os.assert_called_once_with("fakefile")

    mock_open.assert_called_once_with("fake_path", "r", encoding="utf-8")

    assert result == {"test": "test"}


def test_create_object_from_data():
    test_data = [{'name': 'test', 'description': 'fake_fake',
                  'products': [{'name': 'test_dos', 'description': 'test_uno', 'price': 1.1, 'quantity': 5}]}]
    result = create_object_from_data(test_data)
    assert result[0].name == 'test'
    assert result[0].description == 'fake_fake'
    assert result[0].products.rstrip() == 'test_dos, 1.1 руб. Остаток: 5 шт.'
