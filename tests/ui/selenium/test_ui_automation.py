import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestWebUIAutomation:
    """
    UI Test Suite demonstrating Selenium WebDriver automation
    Tests include:
    - Page navigation and loading
    - Form interactions
    - Element verification
    - Cross-browser compatibility concepts
    """
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test"""
        # Setup
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for CI/CD
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        
        yield
        
        # Teardown
        self.driver.quit()
    
    def test_google_search_functionality(self):
        """Test Google search basic functionality"""
        # Navigate to Google
        self.driver.get("https://www.google.com")
        
        # Verify page title
        assert "Google" in self.driver.title
        
        # Find search box and enter search term
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_term = "Selenium WebDriver QA automation"
        search_box.send_keys(search_term)
        
        # Submit search
        search_box.submit()
        
        # Wait for results and verify
        self.wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Verify search results are displayed
        results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")
        assert len(results) > 0, "No search results found"
        
        # Verify URL contains search parameter
        assert "search" in self.driver.current_url or "q=" in self.driver.current_url
    
    def test_page_navigation_and_elements(self):
        """Test navigation and element interaction on example.com"""
        # Navigate to example.com
        self.driver.get("https://example.com")
        
        # Verify page loaded correctly
        assert "Example Domain" in self.driver.title
        
        # Verify main heading
        heading = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert "Example Domain" in heading.text
        
        # Verify paragraph text
        paragraph = self.driver.find_element(By.TAG_NAME, "p")
        assert len(paragraph.text) > 0
        
        # Verify link is present
        link = self.driver.find_element(By.TAG_NAME, "a")
        assert link.is_displayed()
        assert link.get_attribute("href") is not None
    
    def test_form_interaction_demo(self):
        """Test form interaction using HTTPBin forms"""
        # Navigate to HTTPBin forms page
        self.driver.get("https://httpbin.org/forms/post")
        
        # Verify form is present
        form = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        assert form.is_displayed()
        
        # Fill out form fields
        customer_name = self.driver.find_element(By.NAME, "custname")
        customer_name.send_keys("QA Test User")
        
        telephone = self.driver.find_element(By.NAME, "custtel")
        telephone.send_keys("123-456-7890")
        
        email = self.driver.find_element(By.NAME, "custemail")
        email.send_keys("qa.test@example.com")
        
        # Select pizza size
        size_medium = self.driver.find_element(By.XPATH, "//input[@value='medium']")
        size_medium.click()
        
        # Select toppings
        topping_pepperoni = self.driver.find_element(By.XPATH, "//input[@value='pepperoni']")
        topping_pepperoni.click()
        
        # Fill delivery time
        delivery_time = self.driver.find_element(By.NAME, "delivery")
        delivery_time.send_keys("12:00")
        
        # Add comments
        comments = self.driver.find_element(By.NAME, "comments")
        comments.send_keys("This is a test order for QA automation")
        
        # Submit form
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        
        # Verify form submission (HTTPBin shows JSON response)
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
        
        # Verify we're on the result page
        assert "httpbin.org/post" in self.driver.current_url
    
    def test_responsive_design_elements(self):
        """Test responsive design by changing window size"""
        # Test desktop view
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://example.com")
        
        desktop_title = self.driver.find_element(By.TAG_NAME, "h1")
        assert desktop_title.is_displayed()
        
        # Test tablet view
        self.driver.set_window_size(768, 1024)
        time.sleep(1)  # Allow time for responsive changes
        
        tablet_title = self.driver.find_element(By.TAG_NAME, "h1")
        assert tablet_title.is_displayed()
        
        # Test mobile view
        self.driver.set_window_size(375, 667)
        time.sleep(1)  # Allow time for responsive changes
        
        mobile_title = self.driver.find_element(By.TAG_NAME, "h1")
        assert mobile_title.is_displayed()
    
    def test_page_load_performance(self):
        """Test page load performance metrics"""
        start_time = time.time()
        
        self.driver.get("https://example.com")
        
        # Wait for page to fully load
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        
        end_time = time.time()
        load_time = end_time - start_time
        
        # Assert page loads within acceptable time (5 seconds)
        assert load_time < 5.0, f"Page load time {load_time:.2f}s exceeds 5 seconds"
    
    def test_javascript_interaction(self):
        """Test JavaScript execution and interaction"""
        self.driver.get("https://example.com")
        
        # Execute JavaScript to get page title
        page_title = self.driver.execute_script("return document.title;")
        assert "Example Domain" in page_title
        
        # Execute JavaScript to scroll page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Verify scroll position
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        assert scroll_position > 0
    
    @pytest.mark.parametrize("url,expected_title", [
        ("https://example.com", "Example Domain"),
        ("https://httpbin.org", "httpbin.org"),
    ])
    def test_multiple_websites_basic_load(self, url, expected_title):
        """Test basic loading of multiple websites"""
        self.driver.get(url)
        
        # Wait for page to load
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Verify title contains expected text
        assert expected_title.lower() in self.driver.title.lower()
