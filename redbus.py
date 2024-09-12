#Streamlit installation
import streamlit as st
import pymysql as mysql
import pandas as pd

# Database connection
def get_db_connection():
    return mysql.connect(
        host='127.0.0.1',
        user='root',
        password='@@@@@',
        database='redbus_application'
    )

# Insert user data into the database
def insert_user_data(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert query
    insert_query = "INSERT INTO user_details (name, email) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, email))
    
    conn.commit()
    cursor.close()
    conn.close()

# Data fetch filter
def fetch_data(filters, table):
    conn = get_db_connection()
    query = f"SELECT * FROM {table} WHERE 1=1"
    
    # Apply filters
    if filters.get('route_name') and filters['route_name'] != 'No Value':
        query += f" AND route_name LIKE '%{filters['route_name']}%'"
    
    if filters.get('bus_type'):
        bus_types = filters['bus_type']
        bus_type_conditions = ' OR '.join([f"bus_type LIKE '%{bt}%'" for bt in bus_types])
        query += f" AND ({bus_type_conditions})"
    
    if filters.get('starting_time') and filters['starting_time'] != 'No Value':
        start_time, end_time = filters['starting_time'].split(' to ')
        query += f" AND departing_time BETWEEN '{start_time}' AND '{end_time}'"
    
    # Adjust query for rating filter
    rating = filters.get('rating')
    if rating and rating != 'No Value':
        if rating == '1 to 2':
            query += " AND star_rating BETWEEN 1 AND 2"
        elif rating == '2 to 3':
            query += " AND star_rating BETWEEN 2 AND 3"
        elif rating == '3 to 4':
            query += " AND star_rating BETWEEN 3 AND 4"
        elif rating == '4 to 5':
            query += " AND star_rating BETWEEN 4 AND 5"
    
    if filters.get('bus_fare') and filters['bus_fare'] != 'No Value':
        fare_range = filters['bus_fare']
        fare_start, fare_end = fare_range.split(' to ')
        query += f" AND bus_fare BETWEEN {fare_start} AND {fare_end}"
    
    query += ";"
    
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to get route names based on the selected state bus
def get_route_names(table):
    conn = get_db_connection()
    query = f"SELECT DISTINCT route_name FROM {table}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df['route_name'].tolist()


# Store user form submission state
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Home page: Get user details
if not st.session_state['submitted']:
    st.title('Welcome to Red Bus')

    with st.form("user_details_form"):
        Name = st.text_input('Enter your name')
        Email = st.text_input('Enter your email address')

        # Handle form submission
        submitted = st.form_submit_button('Submit')
        if submitted:
            if Name and Email:
                # Store user data in the database
                insert_user_data(Name, Email)
                st.session_state['submitted'] = True
                st.session_state['Name'] = Name
                st.session_state['Email'] = Email
                st.success("Your details have been successfully saved!")
                st.experimental_rerun()
            else:
                st.error("Please fill in both your name and email.")

# Once user has submitted the form, show bus selection options
if st.session_state['submitted']:
    st.sidebar.title('Main Menu')

    selected_option = st.sidebar.radio('Options', ['Home', 'Select Buses'])

    if selected_option == 'Home':
        # Retrieve Name from session state
        st.title(f'Howdy, {st.session_state["Name"]}!')
        st.image('C:/Users/santh/OneDrive/Documents/Redbus/Redbusq.jpg', width=125)
        st.write('### Welcome to Red Bus!')
        st.write('RedBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses. Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. redBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.')
        st.write('## How to book bus tickets')
        st.video('https://www.youtube.com/watch?v=eyAAUGhvZu8')

    elif selected_option == 'Select Buses':
        st.title('Select Buses')

        # Sidebar filters
        st.sidebar.header('Filter Options')
        table_name = st.sidebar.selectbox('Select the state buses name', 
                                          ['apsrtc', 'ksrtc', 'bsrtc', 'rsrtc', 'tsrtc', 'ktcl', 'kaac', 'wbtc', 'pepsu', 'nbstc'])

        # fetch route names
        route_names = get_route_names(table_name)
        route_name = st.sidebar.selectbox('Select the route name', ['No Value'] + route_names)

        # bus type multiselect
        bus_type = st.sidebar.multiselect('Select the bus type', 
                                          ['AC Seater',  'AC Sleeper', 'Non AC Seater', 'Non AC Sleeper'])

        # starting time filter with 24-hour format ranges
        starting_time = st.sidebar.selectbox('Select the departing time', 
                                             ['No Value', '00:00 to 01:00', '01:00 to 02:00', '02:00 to 03:00', '03:00 to 04:00', 
                                              '04:00 to 05:00', '05:00 to 06:00', '06:00 to 07:00', '07:00 to 08:00', 
                                              '08:00 to 09:00', '09:00 to 10:00', '10:00 to 11:00', '11:00 to 12:00', 
                                              '12:00 to 13:00', '13:00 to 14:00', '14:00 to 15:00', '15:00 to 16:00', 
                                              '16:00 to 17:00', '17:00 to 18:00', '18:00 to 19:00', '19:00 to 20:00', 
                                              '20:00 to 21:00', '21:00 to 22:00', '22:00 to 23:00', '23:00 to 24:00'])

        # Rating filter dropdown
        rating = st.sidebar.selectbox('Select the rating', 
                                      ['No Value', '1 to 2', '2 to 3', '3 to 4', '4 to 5'])

        # Updated bus fare input
        bus_fare = st.sidebar.selectbox('Select the bus fare', 
                                        ['No Value', '0 to 500', '500 to 1000', '1000 to 1500', '1500 to 2000', 
                                         '2000 to 2500', '2500 to 3000', '3500 to 4000', '5000 to 6000'])

        filters = {
            'route_name': route_name,
            'bus_type': bus_type,
            'starting_time': starting_time,
            'rating': rating,
            'bus_fare': bus_fare
        }

        # Filters
        st.header(f"{table_name.upper()} Buses")
        bus_data = fetch_data(filters, table_name)
        st.dataframe(bus_data)
    
# Add footer
st.sidebar.markdown("[Red Bus Application](https://www.redbus.in/)")


