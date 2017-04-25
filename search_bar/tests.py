import pytest

# Тестирование введенных данных 
def test_coordinats(latitude, longtitude):
    assert latitude != ''
    assert  longitude != ''
