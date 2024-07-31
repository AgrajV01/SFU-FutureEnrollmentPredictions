# Code for Extracting Data from ratemyprofessor by using web scrapping 

import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import numpy.random

numpy.random.seed(48)

def extract_professor_data(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        name = soup.select_one("div.NameTitle__Name-dowf0z-0").text.strip() if soup.select_one("div.NameTitle__Name-dowf0z-0") else None
        department = soup.select_one("a.TeacherDepartment__StyledDepartmentLink-fl79e8-0").text.strip() if soup.select_one("a.TeacherDepartment__StyledDepartmentLink-fl79e8-0") else None
        quality = soup.select_one("div.CardNumRating__CardNumRatingNumber-sc-17t4b9u-2").text.strip() if soup.select_one("div.CardNumRating__CardNumRatingNumber-sc-17t4b9u-2") else None

        difficulty = None
        would_take_again = None
        feedback_items = soup.find_all("div", class_="FeedbackItem__FeedbackNumber-uof32n-1")
        for item in feedback_items:
            description = item.find_next_sibling("div").text
            if "Level of Difficulty" in description:
                difficulty = item.text.strip()
            elif "Would take again" in description:
                would_take_again = item.text.strip()

        class_name = soup.select_one("div[class*='RatingHeader__StyledClass']").text.strip() if soup.select_one("div[class*='RatingHeader__StyledClass']") else None
        review_date = soup.select_one("div.TimeStamp__StyledTimeStamp-sc-9q2r30-0").text.strip() if soup.select_one("div.TimeStamp__StyledTimeStamp-sc-9q2r30-0") else None

        print(f"Extracted data: Name={name}, Department={department}, Quality={quality}, Difficulty={difficulty}, Would_take_again={would_take_again}, Class={class_name}, Date={review_date}")

        return {
            "Professor_Name": name,
            "Department": department,
            "Quality": quality,
            "Difficulty": difficulty,
            "Would_take_again": would_take_again,
            "Class_Name": class_name,
            "Review_Date": review_date
        }
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return {
            "Professor_Name": None,
            "Department": None,
            "Quality": None,
            "Difficulty": None,
            "Would_take_again": None,
            "Class_Name": None,
            "Review_Date": None
        }

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.ratemyprofessors.com/search/professors/1482?q=*")

    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@class, 'FullPageModal__')]//button"))
        )
        driver.execute_script("arguments[0].click();", close_button)
    except Exception as e:
        print(f"Initial pop-up close button not found: {e}")

    try:
        ad_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='bx-close-inside-1177612']"))
        )
        driver.execute_script("arguments[0].click();", ad_close_button)
    except Exception as e:
        print(f"Ad close button not found: {e}")

    all_professor_data = []

    while True:
        try:
            teacher_cards = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//a[starts-with(@class, 'TeacherCard__StyledTeacherCard')]"))
            )
            urlist = [card.get_attribute("href") for card in teacher_cards]
        except Exception as e:
            print(f"Teacher cards not found: {e}")
            break

        for url in urlist:
            data = extract_professor_data(url)
            all_professor_data.append(data)

        try:
            show_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Show More']"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", show_more_button)
            driver.execute_script("arguments[0].click();", show_more_button)
            time.sleep(1.5)
        except Exception as e:
            print(f"Show More button not found or not clickable: {e}")
            break

    driver.quit()

    df = pd.DataFrame(all_professor_data)
    df.to_csv("professor_ratings_all.csv", index=False)

if __name__ == "__main__":
    main()
