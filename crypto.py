import ccxt
import sys
import pprint
import ssl
import urllib3
from enum import Enum
from collections import OrderedDict, defaultdict, Callable
import requests
import json
import humanize
import datetime
import pytz
import humanize
import time
import telegram_send
import traceback
import pdb
import xmlrpclib

print ccxt.exchanges


#pdb.set_trace()



ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode=ssl.CERT_NONE


ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
tz = pytz.timezone('US/Pacific')
CRYPTOCOMPARE_URL = 'https://min-api.cryptocompare.com/data/pricemultifull'

#Coinbase is not supported bt ccxt
#Coinexchange is not supported bt ccxt
#EtherDelta is not supported bt ccxt
#Tux is not supported bt ccxt and has 0 balance


class DefaultOrderedDict(OrderedDict):
    # Source: http://stackoverflow.com/a/6190500/562769
    def __init__(self, default_factory=None, *a, **kw):
        if (default_factory is not None and
           not isinstance(default_factory, Callable)):
            raise TypeError('first argument must be callable')
        OrderedDict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return OrderedDict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return type(self)(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy
        return type(self)(self.default_factory,
                          copy.deepcopy(self.items()))

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s)' % (self.default_factory,
                                               OrderedDict.__repr__(self))


class non_ccxt_exchange(object):
    def __init__(self, name):
        self.name = name
        self.symbol_quantity_chart = DefaultOrderedDict(list)


    def coin_info(self, symbol, quantity, time=None):
        if time is None:
            time = datetime.datetime.now(tz)

        dict_entry = {"symbol": symbol, "total": float(quantity), "time": time}
        self.symbol_quantity_chart[symbol].append(dict_entry)


    def fetch_balance(self):
        latest_balance = OrderedDict()
        for symbol, symbol_quantity_list in self.symbol_quantity_chart.items():
            latest_balance[symbol] = symbol_quantity_list[-1]

        return latest_balance


    def fetch_ohlcv(self, key_pair, time):
        raise ccxt.NotSupported

class Exchanges(Enum):
    cryptopia = 'Cryptopia'
    bittrex = 'Bittrex'
    yobit = 'YoBit'
    hitbtc = 'HitBTC'
    bitstamp = 'Bitstamp'
    gdax = 'Gdax'
    etherdelta = 'EtherDelta'
    bithumb = 'Bithumb'
    coinexchange = 'Coinexchange'
    coinbase = 'Coinbase'
    binance = 'Binance'
    cobinhood = 'Cobinhood'
    coinex = 'Coinex'
    storiqa = 'Storiqa'
    coinhouse = 'Coinhouse'
    pagarex = 'Pagarex'


cryptopia = ccxt.cryptopia({'apiKey': '7f1e7476a4b2a1f2215f57cadc1af265',
                            'secret': 'oI16wY5N8TKELFy3C0vpeR1Egvxn7+WD3pM45NouI2yPWythHcMRzBsDAXVvGM65kqXl3fRgsOts0vwfoqWGVg==', 'verbose': False})

gdax = ccxt.gdax({'apiKey': '7f1e7476a4b2a1f2215f57cadc1af265',
                            'secret': 'oI16wY5N8TKELFy3C0vpeR1Egvxn7+WD3pM45NouI2yPWythHcMRzBsDAXVvGM65kqXl3fRgsOts0vwfoqWGVg==', 'verbose': False})

gdax = ccxt.gdax({'apiKey': 'a42054a58e1ea4792745046b2f8a10a4',
                  'secret': '6G+rhrRn9bY7kfuuQvumTqH00uMSTdtx4EaF5hndiDvR4eAa8HG+wyTTnvQdKD28YHAEr9TXET2O7oHXg8rWJg==',
                  'verbose': False,
                   'password': 'di3491vw8qo'})

exchange_info = DefaultOrderedDict(list)
exchange_info[Exchanges.gdax].append(gdax)

def ANALYZE_CRYPTO(crypto_dict):
    no_readings = 0
    now_time = datetime.datetime.now(tz)
    variations_list = DefaultOrderedDict(list)
    for name, obj in crypto_dict.items():
        new_time = None
        for time, val in reversed(list(obj.price_chart.items())):
            if new_time is None:
                time_diff = now_time - time
                variations_list[name].append((val, time_diff))
                new_time = time
            else:
                new_time_diff = new_time - time
                variations_list[name].append((val, new_time_diff))
                new_time = time

    global_24h_comparison_vector = DefaultOrderedDict(list)

    for name, val_list in variations_list.items():
        original_value = 0.0000000000
        time_diff_adder = 0.000000000
        most_recent_val = None
        if val_list[0][0] is not None:
            most_recent_val = float(val_list[0][0])

        for tup_obj in val_list:
            if tup_obj[0] is not None:
                original_value = float(tup_obj[0])
                time_diff_adder += tup_obj[1].total_seconds()
                if time_diff_adder > 60*60:
                    break
        if most_recent_val is not None:
            change_percentage = (most_recent_val - original_value) / original_value * 100.0
            global_24h_comparison_vector[name].append((change_percentage,time_diff_adder))

    #Every item in diff_val_list corresponds to 5 minute time from now backwards
    for name, diff_val_tup in reversed(list(global_24h_comparison_vector.items())):
        rank = 'n/a'
        if crypto_dict[name].rank is not None:
            rank = crypto_dict[name].rank

        coinmarketcap_percent_change = 0.00000000
        if len(crypto_dict[name].timeval_diff_chart):
            coinmarketcap_percent_change = next(reversed(crypto_dict[name].timeval_diff_chart.values()))
            if coinmarketcap_percent_change is not None:
                coinmarketcap_percent_change = float(coinmarketcap_percent_change)
            else:
                coinmarketcap_percent_change = 0.00000000
        item = float(diff_val_tup[-1][0])
        diff_time_value = float(diff_val_tup[-1][1])

        if item > 20.0 or coinmarketcap_percent_change > 20.0:
            buy_line = "BUY THIS: " + str(name) + "; 1hour previous inc: " + str(coinmarketcap_percent_change) + '%; present inc: ' + str(item) + '%; happened '+ str(humanize.naturaltime(diff_time_value)) + '; rank: ' + rank
            print(buy_line)
            if crypto_dict[name].ownership is not None:
                print("It is OWNED STOCK")
                #telegram_send.send(messages=['OWNED; ' + buy_line])
            elif int(rank) < 300:
                #telegram_send.send(messages=[buy_line + "; Not Owned"])
                pass

        elif item < -10.0 or coinmarketcap_percent_change < -10.0:
            sell_line = "SELL THIS: " + str(name) + "; 1hour previous inc: " + str(coinmarketcap_percent_change) + '%; present inc: ' + str(item) + '%; happened '+ str(humanize.naturaltime(diff_time_value)) + '; rank: ' + rank
            print(sell_line)
            if crypto_dict[name].ownership is not None:
                print("It is OWNED STOCK")
                #telegram_send.send(messages=['OWNED; ' + sell_line])
            elif int(rank) < 300:
                #telegram_send.send(messages=[sell_line + "; Not Owned"])
                pass

def get_live_exchange_currency(symbol, dest_value='USD', exchange='CCCAGG', price_only=True):
    if type(symbol) != list:
        symbol = [symbol]
    else:
        price_only = False

    if type(dest_value) != list:
        dest_value = [dest_value]
    else:
        price_only = False

    matrix_dict = OrderedDict()

    req_url = CRYPTOCOMPARE_URL + '?' + 'fsyms=' + ','.join(symbol) + '&' + 'tsyms=' + ','.join(dest_value) + '&' + 'e=' + exchange
    print req_url
    response = requests.get(req_url)
    response_dict = json.loads(response.text)
    print(response_dict)
    if 'Response' in response_dict.keys() and response_dict['Response'] == 'Error':
        matrix_dict['Error'] = response_dict['Message']
    else:
        if 'RAW' in response_dict.keys():
            for from_symbol in symbol:
                if from_symbol in response_dict['RAW'].keys():
                    for to_value in dest_value:
                        if to_value in response_dict['RAW'][from_symbol].keys():
                            matrix = response_dict['RAW'][from_symbol][to_value]
                            #print(matrix['MARKET'] + ': ' + str(matrix['PRICE']) + '; TOT MARKET: ' + str(matrix['TOTALVOLUME24HTO']))
                            if price_only:
                                matrix_dict[from_symbol] = matrix['PRICE']
                            else:
                                matrix_dict[exchange] = matrix

    return matrix_dict


#get_live_exchange_currency('BTC', 'USD', 'CCCAGG' , True)

def get_live_exchange_wrapper(key, exchange_name):
    to_symbol_currency_list = ['USD', 'USDT', 'BTC', 'ETH', 'LTC'] #Everything pair should fall under this
    final_out_list = ['USD', 'USDT']

    for to_symbol in to_symbol_currency_list:
        if key != to_symbol:
            actual_balance = get_live_exchange_currency(key, to_symbol, exchange=exchange_name, price_only=True)
            print actual_balance
            if 'Error' not in actual_balance.keys():
                if to_symbol in final_out_list:
                    return float(actual_balance[key])
                else:
                    for final_out_symbol in final_out_list:
                        other_symbol_out_price = get_live_exchange_currency(to_symbol, final_out_symbol, exchange=exchange_name, price_only=True)
                        print "other_symbol_out_price", other_symbol_out_price
                        if 'Error' not in other_symbol_out_price.keys():
                            return float(actual_balance[key]) * float(other_symbol_out_price[to_symbol])

    for to_symbol in to_symbol_currency_list:
        if key != to_symbol:
            actual_balance = get_live_exchange_currency(key, to_symbol, price_only=True)
            print actual_balance
            if 'Error' not in actual_balance.keys():
                if to_symbol in final_out_list:
                    return float(actual_balance[key])
                else:
                    for final_out_symbol in final_out_list:
                        other_symbol_out_price = get_live_exchange_currency(to_symbol, final_out_symbol, price_only=True)
                        if 'Error' not in other_symbol_out_price.keys():
                            return float(actual_balance[key]) * float(other_symbol_out_price[to_symbol])

    return None

#get_live_exchange_wrapper('BTC', 'CCCAGG')


def parse_balance(exchange):
    symbol_dict = OrderedDict()
    for key, vD in exchange.items():
        if type(vD) == dict and 'total' in vD.keys() and vD['total'] > 0:
            symbol_dict[key] = vD
    return symbol_dict


def calculate_balance(exchange_info):

    exchange_name_balance_dict = OrderedDict()


    for exchange_name, vL in exchange_info.items():
        print(exchange_name)
        total_value_dict = OrderedDict()
        actual_balance_value_dict = OrderedDict()
        usd_value_dict = {}

        for exchange in vL:
            try:
                exchange_balance = dict(exchange.fetch_balance())


                exchange_balance_parsed = parse_balance(exchange_balance)
                print "exchange_balance_parsed", exchange_balance_parsed

            except:
                print("Could not calculate the balance for exchange: " + str(exchange_name))
                print(traceback.format_exc())

                continue
            for key, value_dict in exchange_balance_parsed.items():
                if key not in total_value_dict.keys():
                    total_value_dict[key] = float(value_dict['total'])
                else:
                    total_value_dict[key] += float(value_dict['total'])

        for key in total_value_dict.keys():
            if key == 'USDT' or key == 'USD':
                actual_balance_value = float(1.0)
            else:
                try:
                    actual_balance = exchange.fetch_ohlcv(key+'/'+'USD', '1m')
                    #print "actual_balance" , actual_balance


                    #if exchange_name == Exchanges.gdax.value:
                    if exchange_name == gdax:

                        actual_balance_value = float(actual_balance[0][4])
                        print "actual balance", actual_balance_value

                    else:

                        actual_balance_value = float(actual_balance[-1][4])

                except ccxt.NotSupported:
                    actual_balance_value = get_live_exchange_wrapper(key, exchange_name)
                except:
                    try:
                        actual_balance = exchange.fetch_ohlcv(key + '/' + 'USDT', '1h')
                        if exchange_name == Exchanges.gdax.value:
                            actual_balance_value = float(actual_balance[0][4])
                        else:
                            actual_balance_value = float(actual_balance[-1][4])

                    except:
                        print "RUCHIR"
                        btc_usd_price = get_live_exchange_currency('BTC', 'USD', exchange=exchange_name, price_only=True)
                        print "btc_usd_price", btc_usd_price
                        if 'Error' in btc_usd_price.keys():
                            btc_usd_price = get_live_exchange_currency('BTC', 'USDT', exchange=exchange_name, price_only=True)
                            if 'Error' in btc_usd_price.keys():
                                btc_usd_price = get_live_exchange_currency('BTC', 'USD', price_only=True)
                        #actual_balance = exchange.fetch_ohlcv(key + '/' + 'BTC', '1h')
                        if exchange_name == Exchanges.gdax:
                            actual_balance_value = float(actual_balance[0][4]) * float(btc_usd_price['BTC'])
                        else:
                            actual_balance_value = float(actual_balance[-1][4]) * float(btc_usd_price['BTC'])

            actual_balance_value_dict[key] = actual_balance_value
            #print "actual_balance_value", actual_balance_value

            if key == 'USD':
                print( 'Total USD Balance: ' + str(total_value_dict[key]))
            else:
                print(key + ' Market value: ' + str(actual_balance_value) + '; Total Balance  : ' + str(total_value_dict[key]))



            #print(key + '; value: ' + str(actual_balance_value) + '; Total  : ' + str(total_value_dict[key]))

        for key, float_value in total_value_dict.items():
            if key in actual_balance_value_dict.keys() and actual_balance_value_dict[key]:
                total_usd_value = float_value * actual_balance_value_dict[key]
                usd_value_dict[key] = (total_usd_value, float_value)
            else:
                print("Error: Key: " + key + '; exchange: ' + exchange_name)

        exchange_name_balance_dict[exchange_name] = usd_value_dict

    return exchange_name_balance_dict

while True:
    try:
        print ("pl wait...")
        get_live_exchange_wrapper('BTC', 'CCCAGG')

        exchange_name_balance_dict = calculate_balance(exchange_info)

        pprint.pprint(exchange_name_balance_dict)
        print ('\n')

        total_value_in_exchange_dict = OrderedDict()

        coin_worth_in_exchange_dict = OrderedDict()
        for exchange_name, portfolio_dict in exchange_name_balance_dict.items():
            for symbol, (total_value, coin_worth) in portfolio_dict.items():
                if symbol not in total_value_in_exchange_dict.keys():
                    total_value_in_exchange_dict[symbol] = total_value
                    coin_worth_in_exchange_dict[symbol] = coin_worth
                else:
                    total_value_in_exchange_dict[symbol] += total_value
                    coin_worth_in_exchange_dict[symbol] += coin_worth
        msg_string = ''
        msg_string += datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S') + '\n'
        for k, v in coin_worth_in_exchange_dict.items():
            msg_string += k + ' - : ' + str(v) + '; Value: ' + str(total_value_in_exchange_dict[k]) + '; Avg. Cur. Price: '+  str(float(total_value_in_exchange_dict[k])/float(v)) + '\n'
        pprint.pprint(msg_string)

        final_value = float(0)
        for exchange_name, total_value in total_value_in_exchange_dict.items():
            final_value += total_value
        cur_value_str = ("Current value of portfolio: " + str(final_value))
        print ('\n')
        print(cur_value_str)
        #telegram_send.send(messages=[msg_string + '\n' + cur_value_str])
        break
    except KeyboardInterrupt:
        print("Ctrl+C Pressed. Exit")
        break
    except:
        print("excepted. retrying")
        print(traceback.format_exc())
        time.sleep(1000)


