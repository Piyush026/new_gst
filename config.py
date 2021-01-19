from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# PROXY = "14.139.242.252:3128"
# PROXY = "14.63.228.217:80"

def get_chrome_web_driver(options,capabilities):
    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options,desired_capabilities=capabilities)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_browser_in_fullScreen(options):
    options.add_argument("--start-maximized")

def set_automation_adblock(options):
    options.add_extension('Adblock-Plus_v1.4.1.crx')

def set_automation_as_head_less(options):
    options.add_argument('--headless')

def set_proxy(options):
    capabilities = webdriver.DesiredCapabilities.CHROME
    capabilities.setCapability(ChromeOptions.CAPABILITY, options);

def get_driver(options):
    return ChromeDriverManager(options)

API_KEY = '699ec90c07808e7be4d7f128d4a0b3ba'
# URL = 'https://www.expressvpn.com/what-is-my-ip'
URL = 'https://www.knowyourgst.com/gst-number-search/by-name-pan/'
URL1 = 'https://services.gst.gov.in/services/searchtpbypan'
