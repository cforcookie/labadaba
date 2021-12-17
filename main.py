from eth_utils.decorators import combomethod
from web3.main import Web3
from PyQt5 import QtWidgets
import sys
import json
import interface
from web3._utils import personal
import time

class Main(interface.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        global contract, web3
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        web3.isConnected

        address = "0xcdCf95710332281A8d8C02a0ED6025deaD14A85F"

        abi = '[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"admins","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"chanle_require","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"chanle_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"clime_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"confirm_require","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"create_require","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"taker","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes32","name":"code","type":"bytes32"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"string","name":"dyscription","type":"string"},{"internalType":"bool","name":"commision_giver","type":"bool"},{"internalType":"bool","name":"used_shablon","type":"bool"}],"name":"create_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"id_giver","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"id_taker","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"require_to","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"giver","type":"address"},{"internalType":"bool","name":"status","type":"bool"},{"internalType":"bool","name":"chanle","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"shablons","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"catigory","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"transfers","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"giver","type":"address"},{"internalType":"address","name":"taker","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes32","name":"code","type":"bytes32"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"string","name":"dyscription","type":"string"},{"internalType":"bool","name":"commision_giver","type":"bool"},{"internalType":"bool","name":"used_shablon","type":"bool"},{"internalType":"bool","name":"status","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"user_rule","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

        global contract
        contract = web3.eth.contract(abi = abi, address= address)

        self.stackedWidget.setCurrentWidget(self.page)

        # for i in range (len(web3.eth.get_accounts())):
        #     web3.parity.personal.unlockAccount(web3.eth.accounts[i], "", 0)

        global currentAccount
        currentAccount = self.comboBox.currentText()

        self.add_in_list()

        self.pushButton_4.clicked.connect(self.update_all)


    def update_all(self):
        currentAccount = self.comboBox.currentText()  
        self.label.setText((str(web3.eth.getBalance(currentAccount)/10**18) + "ETH"))
        if contract.functions.user_rule(currentAccount).call() == False:
            self.label_2.setText("Пользователь")
        else: 
            self.label_2.setText("Админ")
        
    def add_in_list(self):
        for i in web3.eth.accounts:
            self.comboBox.addItem(i)
            self.comboBox_3.addItem(i)

    def create_transaction(self):
        taker = self.comboBox_3.currentText()  
        value = int(self.lineEdit.text())
        code_word = web3.sha3(text = self.lineEdit_2.text())
        contract.functions.create_transfer(taker, value, code_word, "1", "1", False, False).send({"from" : currentAccount})


def App():
    app = QtWidgets.QApplication(sys.argv)
    web_contract = Main()
    web_contract.show()
    app.exec_()

if __name__ == "__main__":
    App()