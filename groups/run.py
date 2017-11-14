from fb_groups import login, findGroups, leaveGroups
import getpass

def leave():
	username = input("Enter your Facebook username.\n")
	password = getpass.getpass()
	
	keywords = input('''Enter the keywords seperated by space.
Whenever a group name contain any of these keywords the group will be left.\n''').split()
	
	driver = login(username, password)
	if driver.title != "Log in to Facebook | Facebook":
		groups = findGroups(username, driver, keywords)
		leaveGroups(groups, driver)
	else:
		print("Wrong username or password.\n")
	
	driver.close()
	
if __name__=="__main__":
	leave()
