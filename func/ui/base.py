import enum
import uuid
from enum import Enum

from accessify import protected
import allure
import pytest
from allure_commons.types import AttachmentType
from retry import retry
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


@enum.unique
class Feature(Enum):
    """
    TODO
    (Данный комментарий подлежит удалению)
    Необходимо заполнить более релевантыми описаниями действий!
    """
    CHECK_OPEN_PAGE = 'Проверка корректной загрузки страницы'
    CHECK_BUTTON = 'Проверка наличия кнопки'
    CLICK_ELEMENT = 'Нажатие на элемент'
    CHECK_EXIST_ELEMENT = 'Проверка наличия элемента'


@enum.unique
class Title(Enum):
    """
    TODO
    (Данный комментарий подлежит удалению)
    Каждый класс с тестами должен иметь релевантоное название. Необходимо заполнить!
    """
    PROFILE_PAGE = 'Тестирование страницы Профили'
    MAP_PAGE = 'Тестирование страницы Карта'


@enum.unique
class Level(Enum):
    """
    По убыванию - в зависимости от важности
    """
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINER = 'miner'
    TRIVIAL = 'trivial'


@pytest.mark.usefixtures('driver')
class AbstractTest:
    MAIN_PAGE_URL = 'https://planetfor.me/'
    profile_url = 'https://planetfor.me/U3lxe0e'
    driver: WebDriver = None

    def click_element_by_xpath(self, xpath: str) -> bool:
        allure.step('Нажатие на элемент - xpath : {}'.format(xpath))
        element = self.driver.find_element_by_xpath(xpath)
        if element:
            element.click()
            return True
        return False

    def click_element_by_css(self, css_selector: str) -> bool:
        allure.step('Нажатие на элемент - css : {}'.format(css_selector))
        button = self.driver.find_element_by_css_selector(css_selector)
        if button:
            button.click()
            return True
        return False

    @retry(WebDriverException, tries=3, delay=0.3)
    def click_element(self, element: WebElement) -> None:
        if element.is_displayed():
            element.click()

    @retry(WebDriverException, tries=3, delay=0.3)
    def input_text(self, element: WebElement, text: str) -> None:
        if element.is_displayed():
            element.send_keys(text)

    def activate_lens(self) -> bool:
        css_selector = '.ui-icons-search-big'
        self.wait_by_css_selector(css_selector, 2)
        button = self.driver.find_element_by_css_selector(css_selector)
        if button is not None:
            button.click()
            return True
        return False

    def put_text_with_lens(self, some_text: str) -> bool:
        button = self.driver.find_element_by_css_selector('.search-input')
        if button is not None:
            button.click()
            button.send_keys(some_text)
            return True
        return False

    def click_element_by_id(self, element_id: str) -> bool:
        allure.step('Нажатие на элемент - id : {}'.format(element_id))
        self.wait_by_id(element_id, 2)
        button = self.driver.find_element_by_id(element_id)
        if button:
            button.click()
            return True
        return False

    def click_element_by_class_name(self, class_name: str) -> bool:
        allure.step('Нажатие на элемент - class : {}'.format(class_name))
        self.wait_by_class_name(class_name, 2)
        element = self.driver.find_element_by_class_name(class_name)
        if element:
            element.click()
            return True
        return False

    def is_exist_by_class_name(self, class_name) -> bool:
        return len(self.driver.find_elements_by_class_name(class_name)) > 0

    def is_exist_by_css(self, css_name) -> bool:
        return len(self.driver.find_elements_by_css_selector(css_name)) > 0

    def is_exist_by_id(self, id_name) -> bool:
        return len(self.driver.find_elements_by_id(id_name)) > 0

    def is_exist_by_xpath(self, xpath) -> bool:
        return len(self.driver.find_elements_by_xpath(xpath)) > 0

    def is_exist_by_name(self, name) -> bool:
        return len(self.driver.find_elements_by_name(name)) > 0

    def wait_for_correct_current_url(self, desired_url):
        wait.until(lambda driver: driver.current_url == desired_url)

    def wait_by_class_name(self, class_name: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, class_name))
        self.__wait(element_present, timeout)

    def wait_by_id(self, element_id: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        self.__wait(element_present, timeout)

    def wait_by_css_selector(self, css_selector: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        self.__wait(element_present, timeout)

    def __wait(self, element_present, timeout: int) -> None:
        """
        :param timeout: Number of seconds before timing out
        """
        try:
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print('Timed out waiting for page to load')

    def take_screenshot(self, title: str, prefix_name: str) -> None:
        screenshot_name = '{}-{}-screenshot'.format(prefix_name, str(uuid.uuid4()))
        allure.step('Создание снимка экрана - {}'.format(screenshot_name))

        with allure.step(title):
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=screenshot_name,
                          attachment_type=AttachmentType.PNG)
