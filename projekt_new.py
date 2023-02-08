import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from design import Ui_Dialog
import requests
import json
import time
from pycbrf.toolbox import ExchangeRates
import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class BTC_Balance_Checker(QMainWindow, Ui_Dialog):
    btc_cost = 0
    eth_cost = 0
    ltc_cost = 0
    con = sqlite3.connect('projekt_baze.sqlite')
    cur = con.cursor()
    btc = float(cur.execute(f"SELECT amount FROM crypto WHERE name = 'btc'").fetchall()[0][
                    0])  # получаем информацию о сбережениях из базы данных
    eth = float(cur.execute(f"SELECT amount FROM crypto WHERE name = 'eth'").fetchall()[0][0])
    ltc = float(cur.execute(f"SELECT amount FROM crypto WHERE name = 'ltc'").fetchall()[0][0])
    con.commit()
    con.close()
    valut_cost = 1
    valutBadge = '₽'
    a = datetime.today().date()
    rates1 = ExchangeRates(a)
    usd_cost = (str(rates1['USD']).split(',')[4]).split("'")[1]
    eur_cost = (str(rates1['EUR']).split(',')[4]).split("'")[1]
    uah_cost = (str(rates1['UAH']).split(',')[4]).split("'")[1]
    rub_cost = 1

    def __init__(self):  # появляется текст
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.update)
        self.pushButton_7.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.intel)
        self.pushButton_2.clicked.connect(self.valute)
        self.pushButton_4.clicked.connect(self.save)
        self.pushButton_5.clicked.connect(Output_stat)
        self.pushButton_6.clicked.connect(Output_info)
        self.label_12.setText(f'1 BTC = {str(self.get_price("1"))} {self.valutBadge}')
        self.label_13.setText(f'1 LTC = {str(self.get_price("8"))} {self.valutBadge}')
        self.label_14.setText(f'1 ETH = {str(self.get_price("3"))} {self.valutBadge}')
        self.label_8.setText(
            f"У вас {self.btc} BTC это примерно {self.btc_cost} {self.valutBadge},вчера это было {self.valutBadge}")
        self.label_7.setText(
            f"У вас {self.eth} ETH это примерно {self.eth_cost} {self.valutBadge},вчера это было {self.valutBadge}")
        self.label_9.setText(
            f"У вас {self.ltc} LTC это примерно {self.ltc_cost} {self.valutBadge},вчера это было {self.valutBadge}")
        current_datetime = datetime.now()
        time_format = "%H:%M"
        today = f"{current_datetime:{time_format}}"
        self.label_15.setText(f'Время {today}')
        self.update()

    def save(self):  # сохранение в бд
        con = sqlite3.connect('projekt_baze.sqlite')
        cur = con.cursor()
        current_datetime = datetime.now()
        time_format = "%Y-%m-%d %H:%M"
        today = f"{current_datetime:{time_format}}"
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('btc', '{str(self.btc_cost)}{self.valutBadge}','{str(today)}' )")
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('ltc', '{str(self.ltc_cost)}{self.valutBadge}','{str(today)}' )")
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('eth', '{str(self.eth_cost)}{self.valutBadge}','{str(today)}' )")
        con.commit()
        con.close()

    def valute(self):  # стоимость валют
        value1 = self.comboBox.currentText()
        if value1 == 'Euro':
            self.valut_cost = self.eur_cost
            self.valutBadge = '€'
        if value1 == 'Dollar':
            self.valut_cost = self.usd_cost
            self.valutBadge = '$'
        if value1 == 'Rub':
            self.valut_cost = self.rub_cost
            self.valutBadge = '₽'
        if value1 == 'Hryvnia':
            self.valut_cost = self.uah_cost
            self.valutBadge = '₴'
        self.update()

    def new_bd(self):  # работа с бд
        con = sqlite3.connect('projekt_baze.sqlite')
        cur = con.cursor()
        cur.execute(f"UPDATE crypto SET amount = '{str(self.ltc)}' WHERE name = 'ltc'")
        cur.execute(f"UPDATE crypto SET amount = '{str(self.btc)}' WHERE name = 'btc'")
        cur.execute(f"UPDATE crypto SET amount = '{str(self.eth)}' WHERE name = 'eth'")
        con.commit()
        con.close()

    def get_price(self, na):  # получение цены криптовалюты, требует на вход номер криптовалюты с биржи
        url = f"https://api.cryptorank.io/v1/currencies/{na}?api_key=3f249f403056c48cb04d6d011f59c696d6479d64d113d41d8b3d3346c619"
        prev_price = 0
        j = requests.get(url)
        print(j)
        data = json.loads(j.text)
        print(data)
        price = data['data']['values']['USD']['price']
        print(price)
        # return price
        if price != prev_price:
            return int(float(price) * float(self.usd_cost) // float(self.valut_cost))

    def update(self):  # обновление всех показаний
        self.label_12.setText(f'1 BTC = {str(self.get_price("1"))} {self.valutBadge}')
        self.label_13.setText(f'1 LTC = {str(self.get_price("8"))} {self.valutBadge}')
        self.label_14.setText(f'1 ETH = {str(self.get_price("3"))} {self.valutBadge}')
        self.btc_cost = float(self.btc) * int(self.get_price("1"))
        self.eth_cost = float(self.eth) * int(self.get_price("3"))
        self.ltc_cost = float(self.ltc) * int(self.get_price("8"))
        con = sqlite3.connect('projekt_baze.sqlite')
        cur = con.cursor()
        btc_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'btc'").fetchall()[-1]
        ltc_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'ltc'").fetchall()[-1]
        eth_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'eth'").fetchall()[-1]
        con.commit()
        con.close()
        self.label_8.setText(
            f"У вас {self.btc}BTC это примерно {self.btc_cost} {self.valutBadge}, {btc_stat[2][5:10]} в {btc_stat[2][11:]} это было {btc_stat[1]}")
        self.label_7.setText(
            f"У вас {self.eth}ETH это примерно {self.eth_cost} {self.valutBadge}, {eth_stat[2][5:10]} в {eth_stat[2][11:]} это было {eth_stat[1]}")
        self.label_9.setText(
            f"У вас {self.ltc}LTC это примерно {self.ltc_cost} {self.valutBadge}, {ltc_stat[2][5:10]} в {ltc_stat[2][11:]} это было {ltc_stat[1]}")
        old = float(btc_stat[1][:-1]) + float(ltc_stat[1][:-1]) + float(eth_stat[1][:-1])
        self.label_11.setText(
            f"Всего: {self.btc_cost + self.eth_cost + self.ltc_cost} {self.valutBadge}, {ltc_stat[2][5:10]} в {ltc_stat[2][11:]} это было {old} {ltc_stat[1][-1]}")
        current_datetime = datetime.now()
        time_format = "%H:%M"
        today = f"{current_datetime:{time_format}}"

        self.label_15.setText(f'Время {today}')

    def intel(self):  # ввод сбережений пользователя с проверкой на число
        o = self.lineEdit.text()
        value = self.comboBox_2.currentText()
        number = True
        try:
            o = float(o)
        except:
            self.lineEdit.setText('не число')
            number = False
        if value == 'BTC' and number:
            self.btc = o
        if value == 'LTC' and number:
            self.ltc = o
        if value == 'ETH' and number:
            self.eth = o
        self.new_bd()
        self.update()

    def clear(self):  # очистка базы данных
        con = sqlite3.connect('projekt_baze.sqlite')
        cur = con.cursor()
        cur.execute(f"DELETE FROM saved")
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('btc', '0.0₽','0000-00-00 00:00' )")
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('ltc', '0.0₽','0000-00-00 00:00' )")
        cur.execute(
            f"INSERT INTO saved (name, amouth, date) VALUES ('eth', '0.0₽','0000-00-00 00:00' )")
        con.commit()
        con.close()


class Output_stat(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        file_name, ok_pressed = QInputDialog.getText(self, "Введите название", "Как назвать файл?")
        if ok_pressed:
            con = sqlite3.connect('projekt_baze.sqlite')
            cur = con.cursor()
            btc_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'btc'").fetchall()[1:]
            ltc_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'ltc'").fetchall()[1:]
            eth_stat = cur.execute(f"SELECT * FROM saved WHERE name = 'eth'").fetchall()[1:]
            con.commit()
            con.close()
            my_file = open(file_name, "w+", encoding="utf8")
            my_file.write("Тут статистика цены ваших активов\n")
            if btc_stat:
                my_file.write("-----------------BTC------------------\n")
                for i in btc_stat:
                    my_file.write(f"{i[2]}    {i[1]}\n")
                my_file.write("-----------------LTC------------------\n")
                for i in ltc_stat:
                    my_file.write(f"{i[2]}    {i[1]}\n")
                my_file.write("-----------------ETH------------------\n")
                for i in eth_stat:
                    my_file.write(f"{i[2]}    {i[1]}\n")
            else:
                my_file.write('Нет сохранений')
            my_file.close()


class Output_info(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        file_name, ok_pressed = QInputDialog.getText(self, "Введите название", "Как назвать файл ?")
        if ok_pressed:
            con = sqlite3.connect('projekt_baze.sqlite')
            cur = con.cursor()
            btc_info = cur.execute(f"SELECT * FROM info WHERE name = 'btc'").fetchall()
            ltc_info = cur.execute(f"SELECT * FROM info WHERE name = 'ltc'").fetchall()
            eth_info = cur.execute(f"SELECT * FROM info WHERE name = 'eth'").fetchall()
            con.commit()
            con.close()
            my_file = open(file_name, "w+", encoding="utf8")
            my_file.write("Может быть интересно\n")
            my_file.write("-----------------BTC------------------\n")
            my_file.write(f'{btc_info[0][1]}\n')
            my_file.write(f'Дата запуска : {btc_info[0][2]}\n')
            my_file.write("-----------------LTC------------------\n")
            my_file.write(f'{ltc_info[0][1]}\n')
            my_file.write(f'Дата запуска : {btc_info[0][2]}\n')
            my_file.write("-----------------ETH------------------\n")
            my_file.write(f'{eth_info[0][1]}\n')
            my_file.write(f'Дата запуска : {btc_info[0][2]}\n')
            my_file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BTC_Balance_Checker()
    ex.show()
    sys.exit(app.exec_())
