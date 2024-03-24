from bs4 import BeautifulSoup
import requests
import re

def get_atrium_lunch_items():
    # Make the request to the webpage
    bpage_scrape = requests.get("https://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum=13&locationName=The+Atrium&dtdate=3/23/2024&mealName=Lunch+Entree&sName=Rutgers+University+Dining")
    # Check if the request was successful
    if bpage_scrape.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(bpage_scrape.content, 'html.parser')

    # Find all divs with class 'menuBox'
        menu_boxes = soup.find_all('div', class_='menuBox')

        lunch_items = []

        # Iterate over the menu boxes
        for menu_box in menu_boxes:
            # Find the store name
            store_name_tags = menu_box.find_all('p')
            for store_name_tag in store_name_tags:
                store_name = re.sub(r'^--\s*(.*?)\s*--$', r'\1', store_name_tag.find('b').text.strip())
                # Find all divs with class 'col-1' (item names), 'col-2' (portion sizes), and 'col-3' (nutrition links)
                item_names = menu_box.find_all('div', class_='col-1')
                portion_sizes = menu_box.find_all('div', class_='col-2')
                nutrition_links = menu_box.find_all('div', class_='col-3')

                # Iterate over the items to extract the information
                for i in range(len(item_names)):
                    item_name = item_names[i].text.strip()
                    portion_size_text = portion_sizes[i].text.strip()

                    # Extract the integer portion of the size string
                    portion_size = int(re.search(r'\d+', portion_size_text).group())

                    nutrition_link = nutrition_links[i].find('a')['href'] if nutrition_links[i].find('a') else None

                    # Store the information in a dictionary
                    item_info = {
                        'store_name': store_name,
                        'name': item_name,
                        'portion_size': portion_size,
                        'nutrition_link': nutrition_link
                    }

                    # Append the dictionary to the list of all items
                    lunch_items.append(item_info)

    else:
        print("Failed to retrieve the page.")

    for i in range(0, len(lunch_items)):
            link = lunch_items[i]["nutrition_link"]
            url = f"https://menuportal23.dining.rutgers.edu/foodpro/{link}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            nutrition_table = str(soup.find('div', id='nutritional-info'))  # Adjust class name accordingly
            soup2 = BeautifulSoup(nutrition_table, 'html.parser')
            percentages = str(soup2.find_all('ul'))
            soup3 = BeautifulSoup(percentages, 'html.parser')
            nutrients_dict = {}
            for ul in soup3.find_all('ul'):
                for li in ul.find_all('li'):
                    nutrient = li.get_text().strip().split('\n')[0]
                    percentage = int(li.get_text().strip().split('\n')[1].strip().replace('%', '')) if len(li.get_text().strip().split('\n')) > 1 else None
                    nutrients_dict[nutrient] = percentage
            lunch_items[i]["nutrients"] = nutrients_dict


    return lunch_items