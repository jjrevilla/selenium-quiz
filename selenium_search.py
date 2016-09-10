#!/usr/bin/env python
import unittest
from selenium import webdriver


class HealthyChildrenSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_hc_org(self):
        driver = self.driver
        base_url = "https://www.healthychildren.org/English/Pages/default.aspx"
        driver.get(base_url)
        self.assertIn("HealthyChildren.org", driver.title)

        dropdown_container = driver.find_element_by_xpath(
            '/html/body/form/div[9]/div[1]/nav/div/div[2]/ul/li[1]/a[1]/span')
        dropdown_container.click()

        # CHOOSE ANY AGE_STAGE
        age_stage = driver.find_element_by_xpath(
            '/html/body/form/div[9]/div[1]/section[2]/div/div[1]/div[1]/div[2]/div/table/tbody/tr[1]/td/table/tbody/tr/td/a')
        age_stage.click()

        # CHOOSE ANY SUB_AGE_STAGE
        sub_age_stage = driver.find_element_by_xpath(
            '/html/body/form/div[9]/div[1]/section[2]/div/div[1]/div[1]/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a')
        sub_age_stage.click()

        # CHOOSE ANY ARTICLE

        article = driver.find_element_by_xpath(
        '/html/body/form/div[9]/div[1]/section[2]/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]/div/div[2]/ul/li[9]/a')
        article.click()

        # GETTING ARTICLE BODY
        body = driver.find_element_by_xpath(
        '/html/body/form/div[9]/div/section[2]/div/div[2]/div/div/div[3]/div[2]/div[3]/div[3]')
        html_markup = body.get_attribute('innerHTML')

        print html_markup
        

        # GETTING SOURCE

        source = driver.find_element_by_id(
            'ctl00_cphPageContent_lblSource')

        print '================='
        print 'SOURCE OF ARTICLE'
        print source.text


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
