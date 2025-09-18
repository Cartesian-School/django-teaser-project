import sys


def test_addition():
    assert 1 + 1 == 2


def test_python_version():
    # Проверка, что версия Python не ниже 3.11
    major, minor, _ = sys.version_info[:3]
    assert (major, minor) >= (3, 11)
