#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import websocket
import ssl

import json
import requests
import sys


HEADERS = {'user-agent': 'python-developer'} 
TMP = ''



def load_config(config_filename):
	with open(config_filename, 'r') as fd:
		json_data = json.loads(fd.read())

	return json_data


def main(ssl_uri, to_url, login_info, pair, price_type):
	try:
		print('connect to {}'.format(ssl_uri))
		
		ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
		ws.connect(ssl_uri)

		print(ws.recv())

		req = {}
		req["event"] = "subscribe"
		req["channel"] = "ticker"
		req["pair"] = pair

		ws.send(json.dumps(req))
		print(req)

		print(ws.recv())

		print('\n\trecv:\n\n')

		global TMP

		while True:
			recv_list = eval(ws.recv())

			if recv_list[1] != 'hb':
				print("\nreceived from {}:\n{}".format(ssl_uri, recv_list))

				# {"code":"код пары", "quote": актуальная цена}
				payload = {}
				payload["code"] = pair

				if price_type == "BID":
					payload["quote"] = recv_list[1]
				elif price_type == "ASK":
					payload["quote"] = recv_list[4]
				elif price_type == "LAST_PRICE":
					payload["quote"] = recv_list[7]
				else:
					print("[!] Error: unknown price_type: {}".format(price_type))
					sys.exit(1)

				if payload["quote"] != TMP:
					print("\npost request to {}:\n{}\nprice_type: {}\n".format(to_url, payload, price_type))

					r = requests.post(to_url, headers=HEADERS, json=payload, auth=login_info)

					print("\nresponse from {}:".format(to_url))
					print(r.status_code)
					print(r.headers)
					print(r.text)
				else:
					print("{} = {}".format(payload["quote"], TMP))

				TMP = payload["quote"]

				print("\n\n###")


	except KeyboardInterrupt:
		print("\nexit\n")

	except Exception as err:
		print('\nsome error:\n{}\n'.format(err))



if __name__ == "__main__":
	res = load_config('config.json')

	ssl_uri = res.get('ssl_uri')
	to_url = res.get('to_url')
	login_info = (res.get('login'), res.get('pass'))

	pair = res.get('pair')
	price_type = res.get('price_type')
	print(pair, price_type)

	main(ssl_uri, to_url, login_info, pair, price_type)
