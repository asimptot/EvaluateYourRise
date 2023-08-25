from init import *

city = input('Enter your city: \n')
city = city[0].upper() + city[1:]
salary_2022 = int(input('Please enter your salary for the year 2022: \n'))
salary_2023 = int(input('Please enter your salary for the year 2023: \n'))

class GDP:
    def setup(self):
        Setup.init(self)

    def __init__(self):
        self.inexpensive_meal_2022 = 0
        self.inexpensive_meal_2023 = 0
        self.domestic_beer_2022 = 0
        self.domestic_beer_2023 = 0
        self.milk_2022 = 0
        self.milk_2023 = 0
        self.bread_2022 = 0
        self.bread_2023 = 0
        self.egg_2022 = 0
        self.egg_2023 = 0
        self.water_2022 = 0
        self.water_2023 = 0
        self.apple_2022 = 0
        self.apple_2023 = 0
        self.orange_2022 = 0
        self.orange_2023 = 0
        self.potato_2022 = 0
        self.potato_2023 = 0
        self.lettuce_2022 = 0
        self.lettuce_2023 = 0
        self.rice_2022 = 0
        self.rice_2023 = 0
        self.tomato_2022 = 0
        self.tomato_2023 = 0
        self.banana_2022 = 0
        self.banana_2023 = 0
        self.onion_2022 = 0
        self.onion_2023 = 0
        self.cheese_2022 = 0
        self.cheese_2023 = 0
        self.cigarette_2022 = 0
        self.cigarette_2023 = 0
        self.chicken_2022 = 0
        self.chicken_2023 = 0
        self.beef_2022 = 0
        self.beef_2023 = 0
        self.rent_house_2022 = 0
        self.rent_house_2023 = 0
        self.buy_house_2022 = 0
        self.buy_house_2023 = 0
        self.gasoline_2022 = 0
        self.gasoline_2023 = 0
        self.utility_cost_2022 = 0
        self.utility_cost_2023 = 0
        self.internet_2022 = 0
        self.internet_2023 = 0
        self.gym_2022 = 0
        self.gym_2023 = 0
        self.cinema_2022 = 0
        self.cinema_2023 = 0
        self.jeans_2022 = 0
        self.jeans_2023 = 0
        self.dress_2022 = 0
        self.dress_2023 = 0
        self.sport_shoes_2022 = 0
        self.sport_shoes_2023 = 0
        self.business_shoes_2022 = 0
        self.business_shoes_2023 = 0

    def calculate_2022(self):
        sleep(4)
        self.browser.get('https://www.numbeo.com/cost-of-living/city-history/in/'+city)
        sleep(4)

        inexpensive_meal = self.browser.find_element(By.XPATH, '//*[@id="tier_1"]/tbody/tr[1]/td[2]')
        inexpensive_meal_text = inexpensive_meal.text

        if inexpensive_meal_text != '-':
            inexpensive_meal = float(inexpensive_meal_text)
        else:
            print("Invalid inexpensive meal value: '-'")

        domestic_beer = self.browser.find_element(By.XPATH, '//*[@id="tier_3"]/tbody/tr[1]/td[6]')
        domestic_beer_text = domestic_beer.text

        if domestic_beer_text != '-':
            domestic_beer = float(domestic_beer_text)
        else:
            print("Invalid domestic beer value: '-'")

        milk = self.browser.find_element(By.XPATH, '//*[@id="tier_3"]/tbody/tr[1]/td[2]')
        milk_text = milk.text

        if milk_text != '-':
            milk = float(milk_text)
        else:
            print("Invalid milk value: '-'")

        bread = self.browser.find_element(By.XPATH, '//*[@id="tier_3"]/tbody/tr[1]/td[3]')
        bread_text = bread.text

        if bread_text != '-':
            bread = float(bread_text)
        else:
            print("Invalid bread value: '-'")

        egg = self.browser.find_element(By.XPATH, '//*[@id="tier_3"]/tbody/tr[1]/td[4]')
        egg_text = egg.text

        if egg_text != '-':
            egg = float(egg_text)
        else:
            print("Invalid egg value: '-'")

        water = self.browser.find_element(By.XPATH, '//*[@id="tier_3"]/tbody/tr[1]/td[5]')
        water_text = water.text

        if water_text != '-':
            water = float(water_text)
        else:
            print("Invalid water value: '-'")

        apple = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[2]')
        apple_text = apple.text

        if apple_text != '-':
            apple = float(apple_text)
        else:
            print("Invalid apple value: '-'")

        orange = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[3]')
        orange_text = orange.text

        if orange_text != '-':
            orange = float(orange_text)
        else:
            print("Invalid orange value: '-'")

        potato = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[4]')
        potato_text = potato.text

        if potato_text != '-':
            potato = float(potato_text)
        else:
            print("Invalid potato value: '-'")

        lettuce = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[5]')
        lettuce_text = lettuce.text

        if lettuce_text != '-':
            lettuce = float(lettuce_text)
        else:
            print("Invalid lettuce value: '-'")

        rice = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[6]')
        rice_text = rice.text

        if rice_text != '-':
            rice = float(rice_text)
        else:
            print("Invalid rice value: '-'")

        tomato = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[7]')
        tomato_text = tomato.text

        if tomato_text != '-':
            rice = float(tomato_text)
        else:
            print("Invalid tomato value: '-'")

        banana = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[8]')
        banana_text = banana.text

        if banana_text != '-':
            banana = float(banana_text)
        else:
            print("Invalid banana value: '-'")

        onion = self.browser.find_element(By.XPATH, '//*[@id="tier_4"]/tbody/tr[1]/td[9]')
        onion_text = onion.text

        if onion_text != '-':
            onion = float(onion_text)
        else:
            print("Invalid onion value: '-'")

        cheese = self.browser.find_element(By.XPATH, '//*[@id="tier_5"]/tbody/tr[1]/td[2]')
        cheese_text = cheese.text

        if cheese_text != '-':
            cheese = float(cheese_text)
        else:
            print("Invalid cheese value: '-'")

        cigarette = self.browser.find_element(By.XPATH, '//*[@id="tier_5"]/tbody/tr[1]/td[4]')
        cigarette_text = cigarette.text

        if cigarette_text != '-':
            cigarette = float(cigarette_text)
        else:
            print("Invalid cigarette value: '-'")

        chicken = self.browser.find_element(By.XPATH, '//*[@id="tier_5"]/tbody/tr[1]/td[5]')
        chicken_text = chicken.text

        if chicken_text != '-':
            chicken = float(chicken_text)
        else:
            print("Invalid chicken value: '-'")

        beef = self.browser.find_element(By.XPATH, '//*[@id="tier_5"]/tbody/tr[1]/td[6]')
        beef_text = beef.text

        if beef_text != '-':
            beef = float(beef_text)
        else:
            print("Invalid beef value: '-'")

        rent_house = self.browser.find_element(By.XPATH, '//*[@id="tier_6"]/tbody/tr[1]/td[2]')
        rent_house_text = rent_house.text

        if rent_house_text != '-':
            rent_house = float(rent_house_text)
        else:
            print("Invalid rent house value: '-'")

        buy_house = self.browser.find_element(By.XPATH, '//*[@id="tier_7"]/tbody/tr[1]/td[2]')
        buy_house_text = buy_house.text

        if buy_house_text != '-':
            buy_house = float(buy_house_text)
        else:
            print("Invalid buy house value: '-'")

        gasoline = self.browser.find_element(By.XPATH, '//*[@id="tier_9"]/tbody/tr[1]/td[3]')
        gasoline_text = gasoline.text

        if gasoline_text != '-':
            gasoline = float(gasoline_text)
        else:
            print("Invalid gasoline value: '-'")

        utility_cost = self.browser.find_element(By.XPATH, '//*[@id="tier_15"]/tbody/tr[1]/td[2]')
        utility_cost_text = utility_cost.text

        if utility_cost_text != '-':
            utility_cost = float(utility_cost_text)
        else:
            print("Invalid utility cost value: '-'")

        internet = self.browser.find_element(By.XPATH, '//*[@id="tier_15"]/tbody/tr[1]/td[3]')
        internet_text = internet.text

        if internet_text != '-':
            internet = float(internet_text)
        else:
            print("Invalid internet value: '-'")

        gym = self.browser.find_element(By.XPATH, '//*[@id="tier_16"]/tbody/tr[1]/td[2]')
        gym_text = gym.text

        if gym_text != '-':
            gym = float(gym_text)
        else:
            print("Invalid gym value: '-'")

        cinema = self.browser.find_element(By.XPATH, '//*[@id="tier_16"]/tbody/tr[1]/td[4]')
        cinema_text = cinema.text

        if cinema_text != '-':
            cinema = float(cinema_text)
        else:
            print("Invalid cinema value: '-'")

        jeans = self.browser.find_element(By.XPATH, '//*[@id="tier_18"]/tbody/tr[1]/td[2]')
        jeans_text = jeans.text

        if jeans_text != '-':
            jeans = float(jeans_text)
        else:
            print("Invalid jeans value: '-'")

        dress = self.browser.find_element(By.XPATH, '//*[@id="tier_18"]/tbody/tr[1]/td[3]')
        dress_text = dress.text

        if dress_text != '-':
            dress = float(dress_text)
        else:
            print("Invalid dress value: '-'")

        sport_shoes = self.browser.find_element(By.XPATH, '//*[@id="tier_18"]/tbody/tr[1]/td[4]')
        sport_shoes_text = sport_shoes.text

        if sport_shoes_text != '-':
            sport_shoes = float(sport_shoes_text)
        else:
            print("Invalid sport shoes value: '-'")

        business_shoes = self.browser.find_element(By.XPATH, '//*[@id="tier_18"]/tbody/tr[1]/td[5]')
        business_shoes_text = business_shoes.text

        if business_shoes_text != '-':
            business_shoes = float(business_shoes_text)
        else:
            print("Invalid business shoes value: '-'")

        try:
            self.inexpensive_meal_2022 = salary_2022 / inexpensive_meal
            self.domestic_beer_2022 = salary_2022 / domestic_beer
            self.milk_2022 = salary_2022 / milk
            self.bread_2022 = salary_2022 / bread
            self.egg_2022 = salary_2022 / egg
            self.water_2022 = salary_2022 / water
            self.apple_2022 = salary_2022 / apple
            self.orange_2022 = salary_2022 / orange
            self.potato_2022 = salary_2022 / potato
            self.lettuce_2022 = salary_2022 / lettuce
            self.rice_2022 = salary_2022 / rice
            self.tomato_2022 = salary_2022 / tomato
            self.banana_2022 = salary_2022 / banana
            self.onion_2022 = salary_2022 / onion
            self.cheese_2022 = salary_2022 / cheese
            self.cigarette_2022 = salary_2022 / cigarette
            self.chicken_2022 = salary_2022 / chicken
            self.beef_2022 = salary_2022 / beef
            self.rent_house_2022 = salary_2022 / rent_house
            self.buy_house_2022 = salary_2022 / buy_house
            self.gasoline_2022 = salary_2022 / gasoline
            self.utility_cost_2022 = salary_2022 / utility_cost
            self.internet_2022 = salary_2022 / internet
            self.gym_2022 = salary_2022 / gym
            self.cinema_2022 = salary_2022 / cinema
            self.jeans_2022 = salary_2022 / jeans
            self.dress_2022 = salary_2022 / dress
            self.sport_shoes_2022 = salary_2022 / sport_shoes
            self.business_shoes_2022 = salary_2022 / business_shoes
        except:
            sleep(1)

        print('\n\nPurchasing power values for the year 2022: \n\n')
        try:
            print('Inexpensive Meal: ', salary_2022 / inexpensive_meal)
        except:
            sleep(1)
        try:
            print('Domestic Beer: ', salary_2022 / domestic_beer)
        except:
            sleep(1)
        try:
            print('Milk: ', salary_2022 / milk)
        except:
            sleep(1)
        try:
            print('Bread: ', salary_2022 / bread)
        except:
            sleep(1)
        try:
            print('Egg: ', salary_2022 / egg)
        except:
            sleep(1)
        try:
            print('Water: ', salary_2022 / water)
        except:
            sleep(1)
        try:
            print('Apple: ', salary_2022 / apple)
        except:
            sleep(1)
        try:
            print('Orange: ', salary_2022 / orange)
        except:
            sleep(1)
        try:
            print('Potato: ', salary_2022 / potato)
        except:
            sleep(1)
        try:
            print('Lettuce: ', salary_2022 / lettuce)
        except:
            sleep(1)
        print('Rice: ', salary_2022 / rice)
        try:
            print('Tomato: ', salary_2022 / tomato)
        except:
            sleep(1)
        try:
            print('Banana: ', salary_2022 / banana)
        except:
            sleep(1)
        try:
            print('Onion: ', salary_2022 / onion)
        except:
            sleep(1)
        try:
            print('Cheese: ', salary_2022 / cheese)
        except:
            sleep(1)
        try:
            print('Cigarette: ', salary_2022 / cigarette)
        except:
            sleep(1)
        try:
            print('Chicken: ', salary_2022 / chicken)
        except:
            sleep(1)
        try:
            print('Beef: ', salary_2022 / beef)
        except:
            sleep(1)
        try:
            print('Rent House: ', salary_2022 / rent_house)
        except:
            sleep(1)
        try:
            print('Buy House: ', salary_2022 / buy_house)
        except:
            sleep(1)
        try:
            print('Gasoline: ', salary_2022 / gasoline)
        except:
            sleep(1)
        try:
            print('Utility Cost: ', salary_2022 / utility_cost)
        except:
            sleep(1)
        try:
            print('Internet: ', salary_2022 / internet)
        except:
            sleep(1)
        try:
            print('Gym: ', salary_2022 / gym)
        except:
            sleep(1)
        try:
            print('Cinema: ', salary_2022 / cinema)
        except:
            sleep(1)
        try:
            print('Jeans: ', salary_2022 / jeans)
        except:
            sleep(1)
        try:
            print('Dress: ', salary_2022 / dress)
        except:
            sleep(1)
        try:
            print('Sport Shoes: ', salary_2022 / sport_shoes)
        except:
            sleep(1)
        try:
            print('Business Shoes: ', salary_2022 / business_shoes)
        except:
            sleep(1)

    def calculate_2023(self):
        sleep(4)
        self.browser.get('https://www.numbeo.com/cost-of-living/in/'+city)
        sleep(4)

        inexpensive_meal = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[2]/td[2]/span')
        inexpensive_meal_text = inexpensive_meal.text
        numeric_text = re.search(r'[\d.]+', inexpensive_meal_text).group()
        inexpensive_meal = float(numeric_text)

        domestic_beer = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[27]/td[2]/span')
        domestic_beer_text = domestic_beer.text
        numeric_text = re.search(r'[\d.]+', domestic_beer_text).group()
        domestic_beer = float(numeric_text)

        milk = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[11]/td[2]/span')
        milk_text = milk.text
        numeric_text = re.search(r'[\d.]+', milk_text).group()
        milk = float(numeric_text)

        bread = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[12]/td[2]/span')
        bread_text = bread.text
        numeric_text = re.search(r'[\d.]+', bread_text).group()
        bread = float(numeric_text)

        egg = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[14]/td[2]/span')
        egg_text = egg.text
        numeric_text = re.search(r'[\d.]+', egg_text).group()
        egg = float(numeric_text)

        water = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[25]/td[2]/span')
        water_text = water.text
        numeric_text = re.search(r'[\d.]+', water_text).group()
        water = float(numeric_text)

        apple = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[18]/td[2]/span')
        apple_text = apple.text
        numeric_text = re.search(r'[\d.]+', apple_text).group()
        apple = float(numeric_text)

        orange = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[20]/td[2]/span')
        orange_text = orange.text
        numeric_text = re.search(r'[\d.]+', orange_text).group()
        orange = float(numeric_text)

        potato = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[22]/td[2]/span')
        potato_text = potato.text
        numeric_text = re.search(r'[\d.]+', potato_text).group()
        potato = float(numeric_text)

        lettuce = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[24]/td[2]/span')
        lettuce_text = lettuce.text
        numeric_text = re.search(r'[\d.]+', lettuce_text).group()
        lettuce = float(numeric_text)

        rice = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[13]/td[2]/span')
        rice_text = rice.text
        numeric_text = re.search(r'[\d.]+', rice_text).group()
        rice = float(numeric_text)

        tomato = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[21]/td[2]/span')
        tomato_text = tomato.text
        numeric_text = re.search(r'[\d.]+', tomato_text).group()
        tomato = float(numeric_text)

        banana = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[19]/td[2]/span')
        banana_text = banana.text
        numeric_text = re.search(r'[\d.]+', banana_text).group()
        banana = float(numeric_text)

        onion = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[23]/td[2]/span')
        onion_text = onion.text
        numeric_text = re.search(r'[\d.]+', onion_text).group()
        onion = float(numeric_text)

        cheese = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[15]/td[2]/span')
        cheese_text = cheese.text
        numeric_text = re.search(r'[\d.]+', cheese_text).group()
        cheese = float(numeric_text)

        cigarette = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[29]/td[2]/span')
        cigarette_text = cigarette.text
        numeric_text = re.search(r'[\d.]+', cigarette_text).group()
        cigarette = float(numeric_text)

        chicken = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[16]/td[2]/span')
        chicken_text = chicken.text
        numeric_text = re.search(r'[\d.]+', chicken_text).group()
        chicken = float(numeric_text)

        beef = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[17]/td[2]/span')
        beef_text = beef.text
        numeric_text = re.search(r'[\d.]+', beef_text).group()
        beef = float(numeric_text)

        rent_house = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[56]/td[2]/span')
        rent_house_text = rent_house.text
        numeric_text = re.search(r'[\d.]+', rent_house_text).group()
        rent_house = float(numeric_text)

        buy_house = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[61]/td[2]/span')
        buy_house_text = buy_house.text
        numeric_text = re.search(r'[\d.]+', buy_house_text).group()
        buy_house = float(numeric_text)

        gasoline = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[36]/td[2]/span')
        gasoline_text = gasoline.text
        numeric_text = re.search(r'[\d.]+', gasoline_text).group()
        gasoline = float(numeric_text)

        utility_cost = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[40]/td[2]/span')
        utility_cost_text = utility_cost.text
        numeric_text = re.search(r'[\d.]+', utility_cost_text).group()
        utility_cost = float(numeric_text)

        internet = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[42]/td[2]/span')
        internet_text = internet.text
        numeric_text = re.search(r'[\d.]+', internet_text).group()
        internet = float(numeric_text)

        gym = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[44]/td[2]/span')
        gym_text = gym.text
        numeric_text = re.search(r'[\d.]+', gym_text).group()
        gym = float(numeric_text)

        cinema = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[46]/td[2]/span')
        cinema_text = cinema.text
        numeric_text = re.search(r'[\d.]+', cinema_text).group()
        cinema = float(numeric_text)

        jeans = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[51]/td[2]/span')
        jeans_text = jeans.text
        numeric_text = re.search(r'[\d.]+', jeans_text).group()
        jeans = float(numeric_text)

        dress = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[52]/td[2]/span')
        dress_text = dress.text
        numeric_text = re.search(r'[\d.]+', dress_text).group()
        dress = float(numeric_text)

        sport_shoes = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[53]/td[2]/span')
        sport_shoes_text = sport_shoes.text
        numeric_text = re.search(r'[\d.]+', sport_shoes_text).group()
        sport_shoes = float(numeric_text)

        business_shoes = self.browser.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[54]/td[2]/span')
        business_shoes_text = business_shoes.text
        numeric_text = re.search(r'[\d.]+', business_shoes_text).group()
        business_shoes = float(numeric_text)

        self.inexpensive_meal_2023 = salary_2023 / inexpensive_meal
        self.domestic_beer_2023 = salary_2023 / domestic_beer
        self.milk_2023 = salary_2023 / milk
        self.bread_2023 = salary_2023 / bread
        self.egg_2023 = salary_2023 / egg
        self.water_2023 = salary_2023 / water
        self.apple_2023 = salary_2023 / apple
        self.orange_2023 = salary_2023 / orange
        self.potato_2023 = salary_2023 / potato
        self.lettuce_2023 = salary_2023 / lettuce
        self.rice_2023 = salary_2023 / rice
        self.tomato_2023 = salary_2023 / tomato
        self.banana_2023 = salary_2023 / banana
        self.onion_2023 = salary_2023 / onion
        self.cheese_2023 = salary_2023 / cheese
        self.cigarette_2023 = salary_2023 / cigarette
        self.chicken_2023 = salary_2023 / chicken
        self.beef_2023 = salary_2023 / beef
        self.rent_house_2023 = salary_2023 / rent_house
        self.buy_house_2023 = salary_2023 / buy_house
        self.gasoline_2023 = salary_2023 / gasoline
        self.utility_cost_2023 = salary_2023 / utility_cost
        self.internet_2023 = salary_2023 / internet
        self.gym_2023 = salary_2023 / gym
        self.cinema_2023 = salary_2023 / cinema
        self.jeans_2023 = salary_2023 / jeans
        self.dress_2023 = salary_2023 / dress
        self.sport_shoes_2023 = salary_2023 / sport_shoes
        self.business_shoes_2023 = salary_2023 / business_shoes

        print('\n\nPurchasing power values for the year 2023: \n\n')
        print('Inexpensive Meal: ', self.inexpensive_meal_2023)
        print('Domestic Beer: ', salary_2023 / domestic_beer)
        print('Milk: ', salary_2023 / milk)
        print('Bread: ', salary_2023 / bread)
        print('Egg: ', salary_2023 / egg)
        print('Water: ', salary_2023 / water)
        print('Apple: ', salary_2023 / apple)
        print('Orange: ', salary_2023 / orange)
        print('Potato: ', salary_2023 / potato)
        print('Lettuce: ', salary_2023 / lettuce)
        print('Rice: ', salary_2023 / rice)
        print('Tomato: ', salary_2023 / tomato)
        print('Banana: ', salary_2023 / banana)
        print('Onion: ', salary_2023 / onion)
        print('Cheese: ', salary_2023 / cheese)
        print('Cigarette: ', salary_2023 / cigarette)
        print('Chicken: ', salary_2023 / chicken)
        print('Beef: ', salary_2023 / beef)
        print('Rent House: ', salary_2023 / rent_house)
        print('Buy House: ', salary_2023 / buy_house)
        print('Gasoline: ', salary_2023 / gasoline)
        print('Utility Cost: ', salary_2023 / utility_cost)
        print('Internet: ', salary_2023 / internet)
        print('Gym: ', salary_2023 / gym)
        print('Cinema: ', salary_2023 / cinema)
        print('Jeans: ', salary_2023 / jeans)
        print('Dress: ', salary_2023 / dress)
        print('Sport Shoes: ', salary_2023 / sport_shoes)
        print('Business Shoes: ', salary_2023 / business_shoes)

    def compare(self, item_2022, item_2023):
        price_difference = item_2023 - item_2022
        return price_difference

    def close_browser(self):
        Setup.close_browser(self)

gdp = GDP()
gdp.setup()
gdp.calculate_2022()
gdp.calculate_2023()

print('\nPrice differences between 2022 and 2023:\n')

inexpensive_meal_diff = gdp.compare(gdp.inexpensive_meal_2022, gdp.inexpensive_meal_2023)
domestic_beer_diff = gdp.compare(gdp.domestic_beer_2022, gdp.domestic_beer_2023)
milk_diff = gdp.compare(gdp.milk_2022, gdp.milk_2023)
bread_diff = gdp.compare(gdp.bread_2022, gdp.bread_2023)
egg_diff = gdp.compare(gdp.egg_2022, gdp.egg_2023)
water_diff = gdp.compare(gdp.water_2022, gdp.water_2023)
apple_diff = gdp.compare(gdp.apple_2022, gdp.apple_2023)
orange_diff = gdp.compare(gdp.orange_2022, gdp.orange_2023)
potato_diff = gdp.compare(gdp.potato_2022, gdp.potato_2023)
lettuce_diff = gdp.compare(gdp.lettuce_2022, gdp.lettuce_2023)
rice_diff = gdp.compare(gdp.rice_2022, gdp.rice_2023)
tomato_diff = gdp.compare(gdp.tomato_2022, gdp.tomato_2023)
banana_diff = gdp.compare(gdp.banana_2022, gdp.banana_2023)
onion_diff = gdp.compare(gdp.onion_2022, gdp.onion_2023)
cheese_diff = gdp.compare(gdp.cheese_2022, gdp.cheese_2023)
cigarette_diff = gdp.compare(gdp.cigarette_2022, gdp.cigarette_2023)
chicken_diff = gdp.compare(gdp.chicken_2022, gdp.chicken_2023)
beef_diff = gdp.compare(gdp.beef_2022, gdp.beef_2023)
rent_house_diff = gdp.compare(gdp.rent_house_2022, gdp.rent_house_2023)
buy_house_diff = gdp.compare(gdp.buy_house_2022, gdp.buy_house_2023)
gasoline_diff = gdp.compare(gdp.gasoline_2022, gdp.gasoline_2023)
utility_cost_diff = gdp.compare(gdp.utility_cost_2022, gdp.utility_cost_2023)
internet_diff = gdp.compare(gdp.internet_2022, gdp.internet_2023)
gym_diff = gdp.compare(gdp.gym_2022, gdp.gym_2023)
cinema_diff = gdp.compare(gdp.cinema_2022, gdp.cinema_2023)
jeans_diff = gdp.compare(gdp.jeans_2022, gdp.jeans_2023)
dress_diff = gdp.compare(gdp.dress_2022, gdp.dress_2023)
sport_shoes_diff = gdp.compare(gdp.sport_shoes_2022, gdp.sport_shoes_2023)
business_shoes_diff = gdp.compare(gdp.business_shoes_2022, gdp.business_shoes_2023)

print('Inexpensive Meal Difference:', inexpensive_meal_diff)
print('Domestic Beer Difference:', domestic_beer_diff)
print('Milk Difference:', milk_diff)
print('Bread Difference:', bread_diff)
print('Egg Difference:', egg_diff)
print('Water Difference:', water_diff)
print('Apple Difference:', apple_diff)
print('Orange Difference:', orange_diff)
print('Potato Difference:', potato_diff)
print('Lettuce Difference:', lettuce_diff)
print('Rice Difference:', rice_diff)
print('Tomato Difference:', tomato_diff)
print('Banana Difference:', banana_diff)
print('Onion Difference:', onion_diff)
print('Cheese Difference:', cheese_diff)
print('Cigarette Difference:', cigarette_diff)
print('Chicken Difference:', chicken_diff)
print('Beef Difference:', beef_diff)
print('Rent House Difference:', rent_house_diff)
print('Buy House Difference:', buy_house_diff)
print('Gasoline Difference:', gasoline_diff)
print('Utility Cost Difference:', utility_cost_diff)
print('Internet Difference:', internet_diff)
print('Gym Difference:', gym_diff)
print('Cinema Difference:', cinema_diff)
print('Jeans Difference:', jeans_diff)
print('Dress Difference:', dress_diff)
print('Sport Shoes Difference:', sport_shoes_diff)
print('Business Shoes Difference:', business_shoes_diff)

gdp.close_browser()