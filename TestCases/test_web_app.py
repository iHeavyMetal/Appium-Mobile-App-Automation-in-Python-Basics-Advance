import time

from appium import webdriver

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get("http://sadistic.pl")

print(driver.title)

time.sleep(3)
driver.quit()