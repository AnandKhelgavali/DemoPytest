import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_py01:
    @pytest.mark.group1
    def test_sum_005(self):
        a = 2
        b = 8
        sum = a + b
        print("sum -- >" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False
    @pytest.mark.group1
    def test_mum_002(self):
        a = 2
        b = 4
        mul = a * b
        print("mum --->" +str(mul))
        if mul == 8:
            assert True
        else:
            assert False

    @pytest.mark.group2
    @pytest.mark.group3
    def test_credence_007(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "opencall").click()

        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p/a"))
        time.sleep(2)
        list =[]
        for r in range (1, l+1):
            MobileNumber = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p/a["+str(r)+"]").text
            #print("MobileNumber-->" + str(r)+"-->" + str(MobileNumber))
            list.append(MobileNumber)
        print(list)
        if "+91 9091929355" in list:
            print("Mobile number is present")
            print(list.index("+91 9091929355"))
            assert True
        else:
            print("Mobile number is not present")
            assert False
        driver.quit()