# Redbus-Interactive-application
Data scarping, Database management and Filtering &amp; Analyzing with Streamlit 

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

