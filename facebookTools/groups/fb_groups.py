from selenium import webdriver
import getpass

def login(username, password):
	driver = webdriver.Chrome()
	driver.get("https://www.facebook.com")
	
	username_entry = driver.find_element_by_css_selector('input[type="email"]')
	username_entry.send_keys(username)
	
	password_entry = driver.find_element_by_css_selector('input[type="password"]')
	password_entry.send_keys(password)
	
	login_button = driver.find_element_by_css_selector('input[value="Log In"]')
	login_button.click()
	
	return driver

def findGroups(username, driver, keywords):
	fb_groups = "https://www.facebook.com/" + username + "/groups"
	driver.get(fb_groups)
	
	#Scroll to the bottom of the page
	while driver.find_element_by_tag_name('div'):
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    Divs = driver.find_element_by_tag_name('div').text
	    if 'More About You' in Divs:
	        break
		
	all_groups = driver.find_elements_by_css_selector('div[class="mbs fwb"]')
	group_links = []
	print('''Here are the names of the groups to be left.\n''')
	
	for group in all_groups:
		name = group.text
		lower_name = name.lower()
		#Find if the name of the group contains required keyword
		for key in keywords:
			if lower_name.find(key) != -1:
				print(name)
				inside = group.find_element_by_css_selector('a')
				link = inside.get_attribute("href")
				group_links.append(link)
				break
	
	return group_links

def leaveGroups(group_links, driver):
	print("Leaving groups...")
	count_of_groups = len(group_links)
	
	if count_of_groups==0:
		print("No groups found with the given keywords.\n")
		return

	for link in group_links:
		driver.get(link + "leave")
		try:
			leave_button = driver.find_element_by_css_selector('button[class^="_42ft _4jy0 layerConfirm groupsLeaveButton uiOverlayButton"]')
			leave_button.click()
		except:
			continue

def leave():
	username = input("Enter your Facebook username.\n")
	password = getpass.getpass()
	
	keywords = input('''Enter the keywords separated by space.
Whenever a group name contain any of these keywords the group will be left.\n''').split()
	
	driver = login(username, password)
	if driver.title != "Log in to Facebook | Facebook":
		groups = findGroups(username, driver, keywords)
		leaveGroups(groups, driver)
	else:
		print("That's an error!!\nWrong username or password.")
	
	driver.close()
