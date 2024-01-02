driver=webdriver.chrome()
driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
draggable_elements=driver.find_element_by_id("draggable")
droppable_elements=driver.find_element_by_id("droppable")
actions=ActionChains(driver)
actions.drag_and_drop(draggable_elements, droppable_elements).perform()
driver.quit()