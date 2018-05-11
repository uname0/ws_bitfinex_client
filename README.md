# ws_bitfinex_client


#### python version:
	Python 3.6.5

#### tested on:
	Linux arch 4.16.6-1-ARCH


### Installation
	$ git clone https://github.com/uname0/ws_bitfinex_client_mod.git
	$ cd ws_bitfinex_client_mod
	$ sudo pip3.6 install -r requirements.txt
	$ chmod +x client.py

	отредактировать конфиг в файле config.json. добавить адресс(to_url), логин(login) и пас(pass) для авторизации на сервере.
	также добавить торговую пару(pair), которая будет пересылаться клиенту и тип цены(price_type).

	$ ./client.py



*Websocket-клиент, регистрируется через API на криптовалютной бирже www.bitfinex.com (настройки в файле config.json), при получении обновления курса заданой валютной пары выполняет HTTP-вызов POST на адрес [to_url] с базовой HTTP-авторизацией [login:pass] и отправляет полученную котировку в виде JSON-объекта {"code":"код пары", "quote": актуальная цена}*
