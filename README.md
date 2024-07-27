# Redbus-Interactive-application
Data scarping, Database management and Filtering &amp; Analyzing with Streamlit 

**SELENIUM WEB SCRAPING**

**Importing Libraries **

selenium.webdriver: The main module for controlling web browsers using Selenium. 
selenium.webdriver.common.by: Provides a way to locate elements within a document. 
selenium.webdriver.support.ui.WebDriverWait: Waits for a condition to be met before proceeding. 
selenium.webdriver.support.expected_conditions: Contains predefined conditions to use with WebDriverWait. 
selenium.webdriver.common.action_chains.ActionChains: Allows complex user interactions such as hovering or clicking multiple elements. 
pandas: For data manipulation and analysis. 
time: Provides various time-related functions, used for sleeping. 


**Function Definitions**
setup_driver --
Initializes a Chrome WebDriver instance.
Maximizes the browser window.
Sets an implicit wait of 10 seconds for elements to be found.

scroll_to_bottom(driver)--
Scrolls to the bottom of the page in a loop until no new content is loaded (i.e., the height of the page remains the same).

get_route_links(driver)--
Scrolls to the bottom of the page to ensure all route elements are loaded.
Extracts route names and links from elements that match the specified XPath.

click_element(driver, by, value)--
Waits for an element to be clickable, scrolls it into view, and clicks it using JavaScript.

get_bus_details(driver, route_name, route_link)--
Clicks all "View Buses" buttons to load bus details.
Scrolls to the bottom of the page to load all bus items.
Extracts details of each bus and stores them in a list.

handle_pagination(driver, base_url)--
Handles pagination on the main page.
Navigates through pages, extracts route links, and fetches bus details from each route.

main(url)--
Initializes the WebDriver.
Calls the handle_pagination function to get all bus details.
Quits the WebDriver.
Saves the collected data to a CSV file.

**Running the Script**
The main function is called with the URL to scrape.
EX: main('https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile')


=======================================================================================================================

**STREAMLIT**

**Importing Libraries**
streamlit: Used for building web applications. 
pymysql: Library to connect and interact with a MySQL database. 
pandas: Library for data manipulation and analysis.


**Database Connection Function**
pymsql/////get_db_connection(): Establishes a connection to the MySQL database using the provided host, user, password, and database name.

**Data Fetching with Filters**
fetch_data(filters, table): Fetches data from the specified table based on the provided filters. Constructs a SQL query dynamically by adding conditions for each filter if they are specified and not set to 'No Value'.

**Getting Route Names**
get_route_names(table): Fetches distinct route names from the specified table to populate the route name filter options.


**Streamlit Application Layout**
Title and Sidebar Menu: Sets up the main title and sidebar menu with options to navigate between 'Home' and 'Select Buses'.
Home Page: Displays a welcome message and a brief description of RedBus.
Select Buses Page: Provides filters for selecting bus data:
Table Name: Dropdown to select the state bus table.
Route Name: Dropdown to select the route name, populated based on the selected table.
Bus Type: Multiselect for bus types.
Starting Time: Dropdown for selecting the departure time range.
Rating: Dropdown for selecting the rating range.
Bus Fare: Dropdown for selecting the bus fare range.
Filters Dictionary: Gathers all selected filters into a dictionary.
Data Fetching and Display: Fetches the filtered data from the database and displays it in a dataframe.
Footer

**Footer**
Adds a footer message in the sidebar.

