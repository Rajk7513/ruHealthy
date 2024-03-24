from bs4 import BeautifulSoup
import requests
import re

# Make the request to the webpage
bpage_scrape = requests.get("https://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=03&locationName=Livingston+Dining+Commons&dtdate=3/25/2024&mealName=Lunch&sName=Rutgers+University+Dining")
if bpage_scrape.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(bpage_scrape.content, 'html.parser')

    # Find the menuBox div
    menu_div = soup.find('div', class_='menuBox')

    # Initialize a list to store lunch items
    lunch_items = []

    # Find all divs with class 'col-1' (item names), 'col-2' (portion sizes), and 'col-3' (nutrition links)
    item_names = menu_div.find_all('div', class_='col-1')
    portion_sizes = menu_div.find_all('div', class_='col-2')
    nutrition_links = menu_div.find_all('div', class_='col-3')

    # Iterate over the items to extract the information
    for i in range(len(item_names)):
        item_name = item_names[i].text.strip()
        portion_size_text = portion_sizes[i].text.strip()

        # Extract the integer portion of the size string
        portion_size = int(re.search(r'\d+', portion_size_text).group())

        nutrition_link = nutrition_links[i].find('a')['href'] if nutrition_links[i].find('a') else None

        # Store the information in a dictionary
        item_info = {
            'name': item_name,
            'portion_size': portion_size,
            'nutrition_link': nutrition_link
        }

        # Append the dictionary to the list
        lunch_items.append(item_info)

    # Print the list of lunch items
    for item in lunch_items:
        print(item)

else:
    print("Failed to retrieve the page.")
