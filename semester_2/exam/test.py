import pytest
from copy import deepcopy

from custom_list import CustomList
from hash_table import HashTable
from builtin_list import BuiltinList
from abstractions import Dict, Set


class Test:
    drivers = [CustomList(), HashTable(5), BuiltinList()]

    @pytest.mark.parametrize("driver", drivers)
    def test_drivers(self, driver):
        driver = deepcopy(driver)

        to_add = [1, 2, 1, 6]

        for value in to_add:
            driver.add(value)
        assert len(driver) == len(to_add)
        assert sorted(list(driver)) == sorted(to_add)

        to_remove = [1, 2, 5]
        to_leave = [1, 6]

        for value in to_remove:
            driver.remove(value)
        assert len(driver) == len(to_leave)
        assert sorted(list(driver)) == sorted(to_leave)

        assert driver.find(6) == 6
        assert driver.find(5) is None

    @pytest.mark.parametrize("driver", drivers)
    def test_dict(self, driver):
        driver = deepcopy(driver)
        d = Dict(driver)

        for key, value in [(1, 6), (2, 7), (1, 5), (6, 8)]:
            d.set(key, value)
        assert sorted(d.items()) == sorted([(2, 7), (1, 5), (6, 8)])

        for key in [2]:
            d.remove(key)
        assert sorted(d.items()) == sorted([(1, 5), (6, 8)])

        for key, value in [(1, 5), (2, None), (6, 8)]:
            assert d.get(key) == value

    @pytest.mark.parametrize("driver", drivers)
    def test_set(self, driver):
        driver = deepcopy(driver)
        d = Set(driver)

        for key in [1, 2, 1, 6]:
            d.add(key)
        for key, response in [(1, True), (2, True), (5, False)]:
            assert d.isin(key) == response

        for key in [1, 2, 5]:
            d.remove(key)
        for key, response in [(1, True), (2, False), (6, True)]:
            assert d.isin(key) == response
