from selenium.webdriver import ActionChains

from func.ui.base import *

main_page = 'https://planetfor.me'
google_play = 'https://play.google.com/store/apps/details?id=com.planet4me'


@allure.title(Title.PROFILE_PAGE)
class TestProfilePage(AbstractTest):

    @allure.feature(Feature.CLICK_ELEMENT)
    @allure.story('Проверка корректности отображения результатов поиска')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_search_panel(self):
        self.driver.get(self.MAIN_PAGE_URL)
        is_lens_activated = self.activate_lens()
        assert is_lens_activated

        """
        (Данный комментарий подлежит удалению)
        При необходимости (для большей информативности) story можно использовать следующим образом
        """
        allure.story('Кликаем на лупу и заполняем поле ввода текстом')
        is_put_text = self.put_text_with_lens('denchig')
        assert is_put_text

        is_clicked = self.click_element_by_css('a.search-item:nth-child(1)')
        assert is_clicked

    @allure.feature(Feature.CLICK_ELEMENT)
    @allure.story('Проверка корректности отображения результатов поиска')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_PFM_button(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('navbar-logo')
        self.take_screenshot('Скриншот страницы', self.driver.current_url)
        assert main_page in self.driver.current_url

    @allure.feature(Feature.CLICK_ELEMENT)
    @allure.story('Проверка наличия строки поиск')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_activate_lens(self):
        self.driver.get(self.profile_url)
        lens = self.activate_lens()
        self.take_screenshot('Скриншот страницы', self.driver.current_url)
        assert lens

    @allure.feature(Feature.CLICK_ELEMENT)
    @allure.story('Проверка работоспособности строки поиск')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_input_text(self):
        self.driver.get(self.profile_url)
        self.activate_lens()
        input_text = self.put_text_with_lens('Moscow')
        self.take_screenshot('результат поиска', self.driver.current_url)
        assert input_text

    @allure.feature(Feature.CHECK_OPEN_PAGE)
    @allure.story('Проверка активации кнопки и перехода в GOOGLE PLAY на страничку'
                  'PLANET FOR ME')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_google_button(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('footer-download-googlestore-ru')
        assert google_play in self.driver.current_url

    @allure.feature(Feature.CHECK_OPEN_PAGE)
    @allure.story('Проверка активации кнопки и перехода в APP STORE на страничку'
                  'PLANET FOR ME')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_apple_button(self):
        self.driver.get(self.profile_url)
        self.click_element_by_css('footer.footer:nth-child(4) > div:nth-child(1) '
                                  '> div:nth-child(2) > a:nth-child(1)')
        self.wait_by_id('ember161', 3)
        app_store = 'https://apps.apple.com/ru/app/planet-for-me/id1321852947'
        assert app_store in self.driver.current_url

    @allure.feature(Feature.CHECK_BUTTON)
    @allure.story('Проверка наличия кнопки Sharing')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button(self):
        self.driver.get(self.profile_url)
        self.is_exist_by_id('icon-menu')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия кнопки Facebook')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button1(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.is_exist_by_class_name('facebook')

    @allure.feature(Feature.CLICK_ELEMENT)
    @allure.story('Проверка наличия кнопки Facebook')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button1_1(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.click_element_by_class_name('facebook')
        fb = 'https://www.facebook.com'
        assert fb in self.driver.current_url

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия кнопки VK')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button2(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.is_exist_by_class_name('vk')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия кнопки Twitter')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button3(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.is_exist_by_class_name('twitter')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия кнопки mail')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button4(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.is_exist_by_class_name('email')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия кнопки отмена')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_sharing_button5(self):
        self.driver.get(self.profile_url)
        self.click_element_by_class_name('ui-icons-share')
        self.is_exist_by_class_name('action-sheet-group-cancel')

    @allure.feature(Feature.CHECK_BUTTON)
    @allure.story('Проверка наличия кнопки options')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button(self):
        self.driver.get(self.profile_url)
        self.is_exist_by_id('icon-menu')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка работоспособности кнопки Options - '
                  'наличие отображения области логина пользователя')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button1(self):
        self.driver.get(self.profile_url)
        self.click_element_by_id('icon-menu')
        self.is_exist_by_class_name('action-sheet-group-header')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка работоспособности кнопки Options - '
                  'наличие кнопки показать на карте')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button2(self):
        self.driver.get(self.profile_url)
        self.click_element_by_id('icon-menu')
        self.is_exist_by_class_name('action-sheet-group-item')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка работоспособности кнопки Options - '
                  'наличие кнопки отмена ')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button3(self):
        self.driver.get(self.profile_url)
        self.click_element_by_id('icon-menu')
        self.is_exist_by_class_name('action-sheet-group-cancel')

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка работоспособности кнопки Options - '
                  'нажатие кнопки показать на карте')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button2_1(self):
        self.driver.get(self.profile_url)
        self.click_element_by_id('icon-menu')
        self.click_element_by_class_name('action-sheet-group-item')
        map_page = 'https://planetfor.me/U3lxe0e/map'
        assert map_page in self.driver.current_url

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка работоспособности кнопки Options - '
                  'нажатие кнопки отмена ')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_options_button3_1(self):
        self.driver.get(self.profile_url)
        self.click_element_by_id('icon-menu')
        self.click_element_by_class_name('action-sheet-group-cancel')
        assert self.profile_url

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка наличия карты на странице профиля')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_profile_map(self):
        self.driver.get(self.profile_url)
        profile_map = self.is_exist_by_class_name('map-container-moved')
        assert profile_map

    @allure.feature(Feature.CHECK_EXIST_ELEMENT)
    @allure.story('Проверка корректного перехода на карту профиля')
    @allure.severity(severity_level=Level.CRITICAL)
    def test_profile_map(self):
        self.driver.get(self.profile_url)
        self.click_element_by_css('.map-container-moved')
        # map_page = 'https://planetfor.me/U3lxe0e/map'
        # assert map_page in self.driver.current_url

    # @allure.feature('click and drugNdrop photos')
    # @allure.story('Переключение фото')
    # @allure.severity(severity_level=Level.NORMAL)
    # def test_click_description(self):
    #     """
    #     TODO
    #     (Данный комментарий подлежит удалению)
    #     В декораторах данного теста  изменить feature и story.
    #     Нужно еще учитывать тот факт, что элементов 5.
    #     Стоит проверить поле 5/5 - оттуда взять значение и по нему проверить.
    #     Это на TODO!
    #     """
    #
    #     profile_url = 'https://planetfor.me/RD796A5'
    #     """
    #     (Данный комментарий подлежит удалению)
    #     Чтобы более корректно работал тест, нужно profile_url формировать из существующих id объекта (RD796A5)
    #     (Либо через поиск его находить, либо через запрос к БД)
    #     """
    #     self.driver.get(profile_url)
    #     is_clicked = self.click_element_by_class_name('layout-poi-pic')
    #     assert is_clicked
    #
    #     i = 1
    #     slider_center_class_name = 'slick-center'
    #     while i < 5:
    #         i = i + 1
    #         action = ActionChains(self.driver)
    #         self.wait_by_class_name(slider_center_class_name, 2)
    #         is_exist_selector = self.driver.find_element_by_class_name(slider_center_class_name)
    #         assert is_exist_selector
    #
    #         position_x = is_exist_selector.location.get('x')
    #         position_y = is_exist_selector.location.get('y')
    #         action.click_and_hold(is_exist_selector).move_by_offset(-position_x / 2, position_y).release().perform()
    #
    #     is_close_click = self.click_element_by_id('slider')
    #     assert is_close_click
    #
    #     is_exist_selector = self.is_exist_by_class_name(slider_center_class_name)
    #     assert is_exist_selector is False
