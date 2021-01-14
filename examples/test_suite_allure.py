''' This test suite contains 2 passing tests and 2 failing tests. '''

import allure
import pytest
from seleniumbase import BaseCase


class MyTestSuite(BaseCase):

    @allure.title("Тест 1")
    def test_1(self):
        with allure.step("test1_step1"):
            self.open("https://xkcd.com/1664/")

        with allure.step("test1_step2"):
            self.assert_text("Mycology", "div#ctitle", timeout=4)

        with allure.step("test1_step3"):
            for p in range(3):
                self.click('a[rel="next"]')
            self.assert_text("Algorithms", "div#ctitle", timeout=4)

    @pytest.mark.expected_failure
    @allure.title("Тест 2")
    def test_2(self):
        with allure.step("test2_step1"):
            print("\n(This test fails on purpose)")
            self.open("https://xkcd.com/1675/")
            raise Exception("FAKE EXCEPTION: This test fails on purpose.")

    @allure.title("Тест 3")
    def test_3(self):
        self.open("https://xkcd.com/1406/")
        self.assert_text("Universal Converter Box", "div#ctitle", timeout=4)
        self.open("https://xkcd.com/608/")
        self.assert_text("Form", "div#ctitle", timeout=4)

    @pytest.mark.expected_failure
    @allure.title("Тест 4")
    def test_4(self):
        print("\n(This test fails on purpose)")
        self.open("https://xkcd.com/1670/")
        self.assert_element("FakeElement.DoesNotExist", timeout=0.5)
