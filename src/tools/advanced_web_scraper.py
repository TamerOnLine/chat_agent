from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# تحديد المسار الصحيح لـ ChromeDriver
CHROMEDRIVER_PATH = r"C:\Users\Tamer\.wdm\drivers\chromedriver\win64\133.0.6943.141\chromedriver-win32\chromedriver.exe"

def scrape_webpage_selenium(url: str) -> str:
    """
    Uses Selenium to render and extract text content from JavaScript-heavy webpages.
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # تشغيل بدون واجهة رسومية
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-accelerated-2d-canvas")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-webgl")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-usb-keyboard-detect")

        # تشغيل ChromeDriver من المسار المحدد
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # فتح الصفحة المطلوبة
        driver.get(url)
        driver.implicitly_wait(10)

        page_source = driver.page_source
        driver.quit()

        return page_source[:1000] + "..." if len(page_source) > 1000 else page_source

    except Exception as e:
        return f"Error scraping the webpage: {e}"

# تعريف الأداة في LangChain
from langchain.tools import Tool

advanced_web_scraper = Tool(
    name="AdvancedWebScraper",
    func=scrape_webpage_selenium,
    description="Scrapes webpage content using Selenium for JavaScript-heavy pages.",
    return_direct=True,
)
