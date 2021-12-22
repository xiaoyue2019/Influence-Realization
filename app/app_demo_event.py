from eth_typing.encoding import Primitives
from web3 import Web3
from usdt import abi
import time
from pprint import *

class GetEvent():
    def __init__(self) -> None:
        url = "https://kovan.infura.io/v3/34ed41c4cf28406885f032930d670036"
        self.web3 = Web3(Web3.HTTPProvider(url))
        address = self.web3.toChecksumAddress('0x850995f1EA2a542D9e3F1072e34D1A15eF6860F2')
        self.contract = self.web3.eth.contract(address=address, abi=abi)

    def MainFunction(self):
        latest = self.web3.eth.blockNumber
        issueEvents = self.contract.events.Issue.createFilter(fromBlock=0, toBlock=latest)
        data = issueEvents.get_all_entries()
        return data

    def ParsingEvent(self,data):
        issueList = []
        for i in data:
            issueData = {}
            issueData['amount'] = i['args']['amount']
            issueData['address'] = i['address']
            issueData['blockNumber'] = i['blockNumber']
            issueList.append(issueData)
        return issueList

    def getIssueEvents(self,realtime):
        while 1:
            data = self.MainFunction()
            pprint(self.ParsingEvent(data))
            time.sleep(realtime)

    def getIssueEventsPoll(self):
            data = self.MainFunction()
            return(self.ParsingEvent(data))

    def getIssueEventsPollCon(self):
            data = self.ParsingEvent(self.MainFunction())[-1]['amount']
            return data

if __name__ == "__main__":
    getfunc = GetEvent()
    getfunc.getIssueEvents(10)