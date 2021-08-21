from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

'''
The Jisho header exists across all Jisho pages with common functions
so all pages should extend from this one. This class shouldn't be used
for testing but rather a way to create further Jisho page objects
'''
class JishoHeader(BasePage):
    url = 'https://jisho.org'
    ''' CSS selectors for this page '''
    logo_link = '.logo a'
    search_input = '#keyword'
    handwriting_button = '#handwriting_button'
    handwriting_pad = '.panel canvas'
    handwriting_results = '#handwriting_area a.result'
    radical_button = '#radical_button'

    def click_logo_image(self):
        self.wait_for_element(self.logo_link).click()

    def set_search_bar_text(self, kanji):
        search_element = self.wait_for_element(self.search_input)
        # This should probably be encoded unicode?
        search_element.send_keys(kanji)

    def get_search_bar_text(self):
        return self.wait_for_element(self.search_input).get_attribute('value')

    def search_via_enter_button(self):
        search_element = self.wait_for_element(self.search_input)
        # press enter afterwards
        search_element.send_keys('\ue007')

    def open_handwriting_pad(self):
        handwriting_button = self.wait_for_element(self.handwriting_button)
        handwriting_button.click()
    
    def draw_on_handwriting_pad(self, points_list):
        ''' Take in a list of lists of points corresponding to drawn lines '''
        for vertex_list in points_list:
            line_drawer = ActionChains(self.driver)
            # get handwriting pad element
            handwriting_pad = self.wait_for_element(self.handwriting_pad)
            # navigate to first point and remove it from the list
            initial_x, initial_y = vertex_list.pop(0)
            line_drawer.move_to_element(handwriting_pad)
            line_drawer.move_to_element_with_offset(handwriting_pad, initial_x, initial_y)
            # click and hold
            line_drawer.click_and_hold()
            # move mouse to remaining points
            for x, y in vertex_list:
                line_drawer.move_to_element_with_offset(handwriting_pad, x, y)
            # release
            line_drawer.release()
            line_drawer.perform()
        pass

    def get_handwriting_results(self):
        all_kanji = self.wait_for_elements(self.handwriting_results)
        return list(map(lambda x: x.text, all_kanji))