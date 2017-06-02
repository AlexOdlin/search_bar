import pytest
import json
from search_bar import search_bar


def mock_bars_data():
    json_data = '{"Id":"ae3e9479-070f-4d66-9429-de3acd8427ac","Number":1,"Cells":{"global_id":20660594,"Name":"Юнион Джек","IsNetObject":"нет","OperatingCompany":null,"AdmArea":"Центральный административный округ","District":"Мещанский район","Address":"Нижний Кисельный переулок, дом 3, строение 1","PublicPhone":[{"PublicPhone":"(495) 621-19-63"}],"SeatsCount":30,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.621587946152012,55.765366956608361]}}}'
    return json.loads(json_data)


# Тестирование введенных данных
def test_empty_data_input():
    assert search_bar.get_closest_bar([], 0, 0) is None


def test_none_coordinates():
    assert search_bar.get_closest_bar(mock_bars_data(), None, None) is None


def test_negative_coordinates():
    with pytest.raises(SyntaxError):
        search_bar.get_closest_bar([], -3, -4)


def test_non_number_coordinates():
    with pytest.raises(SyntaxError):
        search_bar.get_closest_bar([], "mama", "papa")

