from pageobjects.jisho_header import JishoHeader
from base_page import BasePage
from selenium.webdriver.common.by import By

class JishoResultsPage(JishoHeader):
    ''' CSS selectors for this page '''
    main_results = '#main_results'
    no_matches = '#no-matches'
    exact_match_detail_links = '.exact_block .light-details_link'
    words_found = '#primary span.text'
    word_detail_links = '#primary .light-details_link'

    def __init__(self, driver):
        super(JishoResultsPage, self).__init__(driver)

    def get_all_words(self):
        if not self.element_exists(self.words_found):
            return []
        all_words = self.wait_for_elements(self.words_found)
        return list(map(lambda x: x.text, all_words))

    def wait_for_page_load(self):
        return self.wait_for_element(self.main_results)