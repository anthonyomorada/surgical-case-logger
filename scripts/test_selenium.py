from selenium import webdriver

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Open a webpage
driver.get("https://www.nba.com")

# Print the page title to verify it works
print("Page title is:", driver.title)

# Close the browser
driver.quit()