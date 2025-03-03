![](https://github.com/uchaev508/hmn-simle-reger/blob/c505ddb5474af705f0579edf20ce6d2370428ae7/logos/logo-360x180.png?raw=true)

![](https://img.shields.io/github/stars/Mitchelded/hmn-simple-reger-selenium)
![](https://img.shields.io/github/forks/Mitchelded/hmn-simple-reger-selenium) 
![](https://img.shields.io/github/issues/Mitchelded/hmn-simple-reger-selenium)
![](https://img.shields.io/github/stars/Mitchelded)

- [Актуальный функционал](README.md/#актуальный-функционал)
- [Что требуется для начала?](README.md/#что-требуется-для-начала)
  * [Инструкция по эксплуатации проекта для чайников времен до н.э.](README.md/#инструкция-по-эксплуатации-проекта-для-чайников-времен-до-нэ)

### Актуальный функционал
#### Выполнено:
- [x] Регистрация аккаунта для получения ключа с проверкой IP и почты.
- [x] Постараться найти какой-нибудь почтовый сервис временной почты не заблокированный на HmN и используя API получать письма автоматически (https://docs.mail.tm/ https://mail.zsay.ru/) 

#### В процессе:
- [ ] Реализовать использование API сервиса https://docs.mail.tm/.
- [ ] Добавить использование прокси или VPN.

### Что требуется для начала?
1. Прямые руки
![](https://media.istockphoto.com/photos/two-hands-with-palms-facing-up-picture-id153180923?k=20&m=153180923&s=612x612&w=0&h=ZFG_DjtuLs2VDkxL42KwMP3i1OR9Oa2dYcnl5_TauHc=)
2. Установленный язык программирования Python версии 3.6+
![](https://foto.yenikadin.com/galeri/2012/06/20/piton-ile-ayni-evde-yasiyor_97875_b.jpg)
3. Соблюдение инструкции
![](https://www.meme-arsenal.com/memes/12fe855b73531e0ae1bf4b452734d2f2.jpg)
4. IP адрес должен быть девственным, другими словами чистым  (ранее не получать ключ на HideMyName). В противном случае следует использовать прокси.

### Инструкция по эксплуатации проекта для чайников времен до н.э.
1. Скопировать репозиторий ```git clone https://github.com/Mitchelded/hmn-simple-reger-selenium```
2. Перейти в рабочий каталог ```cd hmn-simple-reger-selenium```
3. Установить необходимые модули для работы воспользовавшись командой 
```pip install -r requirements.txt```
4. Запускаем файл **hmn-simple-reger.py** ```python hmn-simple-reger.py```
5. Если все хорошо - попросит ввести адрес электронной почты
6. После ввода адреса электронной почты должно придти письмо (если адрес не находится в черном списке почт)
7. Копируем ссылку для активации с письма и вставляем в скрипт
8. Готово! Ключ должен придти письмом

### В случае возниковения проблем со скриптом можно создать Issue
Я планирую поддерживать данный скрипт и обновить его по возможности в ближайшем будущем
