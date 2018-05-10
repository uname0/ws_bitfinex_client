# ws_bitfinex_client


python version:
Python 3.6.5

tested on:
Linux arch 4.16.6-1-ARCH


* requirements:
	* certifi==2018.4.16
	* chardet==3.0.4
	* idna==2.6
	* requests==2.18.4
	* six==1.11.0
	* urllib3==1.22
	* websocket-client==0.47.0


* (git clone this repository)
* $ mkvirtualenv ws_bitfinex_client
* $ workon ws_bitfinex_client
* $ pip install websocket-client
* $ pip install requests
* $ chmod +x client.py

* (!!!
	* отредактировать конфиг. добавить адресс(to_url), логин(login) и пас(pass) для авторизации на сервере.
	* также добавить торговую пару(pair), которая будет пересылаться клиенту и тип цены(price_type).
* !!!)

* $ ./client.py



*Websocket-клиент, регистрируется через API на криптовалютной бирже www.bitfinex.com (настройки в файле config.json), при получении обновления курса заданой валютной пары выполняет HTTP-вызов POST на адрес [to_url] с базовой HTTP-авторизацией [login:pass] и отправляет полученную котировку в виде JSON-объекта {"code":"код пары", "quote": актуальная цена}*
