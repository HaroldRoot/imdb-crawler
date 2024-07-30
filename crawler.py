# coding: utf-8
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_year_from_user():
    current_year = datetime.now().year
    while True:
        try:
            year = int(input(f"Enter the year (format: YYYY), range: 1894 to {current_year}: "))
            if 1894 <= year <= current_year:
                return year
            else:
                print(f"Year must be between 1894 and {current_year}. Please enter again.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def main():
    year = get_year_from_user()
    url = f"https://www.imdb.com/search/title/?title_type=feature&release_date={year}-01-01,{year}-12-31"

    driver = webdriver.Chrome()
    driver.get(url=url)
    page_title = driver.title
    print(f'Page title: {page_title}')

    wait = WebDriverWait(driver, 10)

    try:
        num_line = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'ipc-page-grid__item')]//div[contains(text(), '1-')]")
            )
        )
        total_movies = int(num_line.text.split("of")[1].replace(",", "").strip())
        print(f'Total number of movies: {total_movies}')

        iterations = 0
        collected_movies = set()

        while len(collected_movies) < total_movies:
            if iterations > (total_movies / 50) + 1:
                raise RuntimeError("Too many iterations")

            movie_elements = wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'h3.ipc-title__text')
                )
            )

            new_movies = [element.text for element in movie_elements
                          if element.text not in collected_movies and element.text != 'Recently viewed']
            collected_movies.update(new_movies)

            for movie in new_movies:
                print(movie)

            if len(collected_movies) < total_movies:
                see_more_button = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//button[contains(@class, "ipc-see-more__button")]')
                    )
                )
                driver.execute_script("arguments[0].click();", see_more_button)
                time.sleep(5)

            iterations += 1

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
