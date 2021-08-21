from conftest import driver
import pytest
from pageobjects.jisho_home_page import JishoHomePage
from pageobjects.jisho_results_page import JishoResultsPage

@pytest.fixture(scope="module", autouse=True)
def setup(driver):
    global jishoHomePage, jishoResultsPage
    jishoHomePage = JishoHomePage(driver)
    jishoResultsPage = JishoResultsPage(driver)
    # Start at homepage
    jishoHomePage.goto('/')

def test_clicking_logo_clears_search_bar_value():
    ''' logo when clicked should redirect to homepage '''
    jishoHomePage.set_search_bar_text('体')
    jishoHomePage.click_logo_image()
    assert jishoHomePage.get_search_bar_text() == ''

def test_body_kanji_returns_results():
    jishoHomePage.set_search_bar_text('体')
    jishoHomePage.search_via_enter_button()
    jishoResultsPage.wait_for_page_load()
    assert len(jishoResultsPage.get_all_words()) != 0

def test_non_kanji_returns_no_results():
    jishoHomePage.set_search_bar_text('\\')
    jishoHomePage.search_via_enter_button()
    jishoResultsPage.wait_for_page_load()
    assert len(jishoResultsPage.get_all_words()) == 0

# Fails intentionally
@pytest.mark.xfail
def test_valid_kana_returns_no_results():
    jishoHomePage.set_search_bar_text('からだ')
    jishoHomePage.search_via_enter_button()
    jishoResultsPage.wait_for_page_load()
    assert len(jishoResultsPage.get_all_words()) == 0

def test_drawing_body_kanji_gives_correct_result():
    body_kanji_vertices = [[(62, 25), (30, 82)],
                          [(50, 52), (50, 136)],
                          [(81, 51), (141, 51)],
                          [(108, 25), (108, 136)],
                          [(108, 51), (86, 100)],
                          [(108, 51), (136, 100)],
                          [(100, 110), (120, 110)]]
    jishoHomePage.open_handwriting_pad()
    jishoHomePage.draw_on_handwriting_pad(body_kanji_vertices)
    jishoHomePage.wait(1)
    handwriting_results = jishoHomePage.get_handwriting_results()
    assert '体' in handwriting_results