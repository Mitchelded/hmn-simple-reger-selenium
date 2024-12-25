import time
import google_colab_selenium as gs


driver = gs.UndetectedChrome()

try:
    demo_url = 'https://hidemy.io/ru/demo/'
    driver.get(demo_url)
    time.sleep(3)  # Дождаться загрузки страницы
    if "Ваша электронная почта" in driver.page_source:
        email = input('Введите электронную почту для получения тестового периода: ')
        email_input = driver.find_element(By.NAME, "demo_mail")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(3)
        if "Ваш код выслан на почту" in driver.page_source:
            print("Код отправлен на почту. Подтвердите e-mail.")
            confirm = input('Введите ссылку для подтверждения e-mail адреса: ')
            while True:
                try:
                    driver.get(confirm)
                    time.sleep(3)
                    if "Спасибо" in driver.page_source:
                        print("Почта подтверждена. Код отправлен на вашу почту!")
                        break
                    else:
                        confirm = input('Ссылка невалидная, повторите попытку: ')
                except Exception as e:
                    print(f"Ошибка подтверждения ссылки: {e}")
                    confirm = input('Ссылка невалидная, повторите попытку: ')
        else:
            print("Указанная почта не подходит для получения тестового периода.")
    else:
        print("Форма ввода почты не найдена на странице.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    driver.quit()