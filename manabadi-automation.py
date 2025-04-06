import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

def search_hall_ticket(start, end):
    option=webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    service=Service(executable_path="path/to/your/chromedriver.exe")
    driver =webdriver.Chrome(service=service,options=option)
    driver.get("https://www.manabadi.co.in/Entrance-Exams/ap-ecet-results-andhrapradesh-engineering-common-entrance-test-results.asp")

    results = []
    for hall_ticket in range(start, end):
        hall_input = driver.find_element(By.ID, "htno")
        hall_input.send_keys(str(hall_ticket))
        hall_input.clear()

        degree_select = Select(driver.find_element(By.ID, "Degree"))
        degree_select.select_by_value("b")  

        submit_button = driver.find_element(By.ID, "btnsubmit")
        submit_button.click()

        result = []

        results.append(results)

        driver.back()

    driver.quit()
    return results

def write_to_csv(results):
    with open('hall_ticket_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Hall Ticket Number", "Result"]) 
        for result in results:
            writer.writerow([result[0], result[1]])  

start_time = time.time()

# Create 10 threads
threads = []
for i in range(5):
    start = 419603010 + i * 10
    end = 419603010 + (i + 1) * 10
    t = threading.Thread(target=search_hall_ticket, args=(start, end))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

