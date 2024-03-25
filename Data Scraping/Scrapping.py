# Importing required libraries
import pandas as pd
import time

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Update the Webdriver_manager using the comands form the ReadMe file.

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Initialize the GeckoDriver service using WebDriverManager
service = Service(executable_path=GeckoDriverManager().install())

# Set Firefox options (optional)
options = webdriver.FirefoxOptions()

# Initialize the Firefox driver with the service and options
driver = webdriver.Firefox(service=service, options=options)

# Navigate to the Billboard Hot 100 chart
driver.get("https://www.billboard.com/charts/hot-100/")

# Example: Creating a list of years from 2019 to 2022
start_year = 2019
end_year = 2022

# Example: Using a while loop to generate a list of years from start_year to end_year
years = []
year = start_year
while year <= end_year:
    years.append(str(year))
    year += 1

# Close the browser window
driver.quit()

from selenium.webdriver.common.by import By

# Dictionary to store name of artists
artists_data = {}

# Dictionary to store top 100 songs
songs_data = {}

# Initialize index for iterating through dates
index = 0
while index < len(dates):
    j = dates[index]
    link = "https://www.billboard.com/charts/hot-100/{}-07-01/".format(j)
    driver.implicitly_wait(10)
    driver.get(link)

    # Container for referencing the division with top 100 songs
    div = driver.find_elements(By.CLASS_NAME, 'o-chart-results-list-row-container')
    songs, artists = [], []
    print(j)
    
    # Initialize index for iterating through div elements
    i = 0
    while i < len(div):
        # Getting the song name
        song = div[i].find_element(By.CSS_SELECTOR, 'li ul li h3').text
        # Getting the artist name
        name = div[i].find_element(By.CSS_SELECTOR, 'li ul li span').text
        # Appending the song and artist name to the lists
        songs.append(song)
        artists.append(name)
        
        # Move to the next div element
        i += 1

    artists_data[j] = artists
    songs_data[j] = songs
    
    # Move to the next date
    index += 1

# Terminating a session and closing the active browser
driver.close()

service = Service(executable_path=GeckoDriverManager().install())
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

# Browsing to Google
driver.get("https://www.google.com")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Dataframe to store the song, artist, lyrics, release year, and genre
df = pd.DataFrame(columns=['Top100Year', 'SongTitle', 'Artist', 'LyricsStatus', 'Lyrics', 'ReleaseYear', 'Genre'])

# Fetching song lyrics for top 100 songs
for year in songs_data.keys():
    songs_list = songs_data[year]
    artists_list = artists_data[year]
    
    print(year)
    for song, artist in zip(songs_list, artists_list):
        # Selenium WebDriverWait is one of the Explicit waits.
        # Explicit waits are confined to a particular web element.
        # Explicit Wait is code you define to wait for a certain condition to occur before proceeding further in the code.
        # It is applied on certain element with defined expected condition and time.
        # This wait is only applied to the specified element. This wait can also throw exception when element is not found.
        # Here we will wait for the google search button element to be clickable.
        # https://www.softwaretestingmaterial.com/webdriverwait-selenium-webdriver/
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
        # Entering the search text
        element.send_keys(f"{artist} {song} lyrics")
        # Submiting the form for google search
        element.submit()
        # To prevent captcha being initialized due to bot activity
        time.sleep(10)
        try:
            # Fetching the default lyrics fetched by google using 'lyricfind'
            lyric = driver.find_element(By.CLASS_NAME, 'xaAUmb').text
            # If default lyrics is available, set lyricstatus to True
            # Lyric Status True indicates lyrics are available
            status = True
        except:
            # If default lyrics is not available, set lyricstatus to False
            # Lyric Status False indicates lyrics are not available
            status = False
            lyric = None
        try:
            # Fetching genre and release year of the song
            info = driver.find_elements(By.CSS_SELECTOR, 'div.rVusze')
            release_year = next((i.find_element(By.CLASS_NAME, 'LrzXr').text for i in info if i.find_element(By.CLASS_NAME, 'w8qArf').text == 'Released:'), None)
            genre = next((i.find_element(By.CLASS_NAME, 'LrzXr').text for i in info if i.find_element(By.CLASS_NAME, 'w8qArf').text == 'Genres:'), None)
        except:
            # If genre and year information is not available
            release_year = None
            genre = None
        # Adding the song, artist and lyrics to dataframe
        df = df.append({'Top100Year': year, 'SongTitle': song, 'Artist': artist, 'LyricsStatus': status, 'Lyrics': lyric, 'ReleaseYear': release_year, 'Genre': genre}, ignore_index=True)
        # Browsing back to Google search home page
        driver.back()


# Terminating a session and closing the active browser
driver.close()

# Display the dataframe
print(df)

# Converting DataFrame to CSV
df.to_csv('billboard_2019_to_2023_top_100_song_lyrics.csv', index=False)