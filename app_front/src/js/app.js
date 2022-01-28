App = {
  web3Provider: null,
  riskMonitoring: null,

  init: function() {
    return App.initWeb3();
  },

  initWeb3: function() {
    // If there is injected web3
    if(typeof web3 !== 'undefined') {
      App.web3Provider = web3.currentProvider;
    } else {
      // Else fallback to kovan
      App.web3Provider = new Web3.providers.HttpProvider('https://kovan.infura.io/v3/34ed41c4cf28406885f032930d670036');
    }
    web3 = new Web3(App.web3Provider);
    return App.initContract();
  },

  initContract: function() {
    $.getJSON('risk-monitoring.json', function(data) {
      // Retrieve data, init truffle contract
      App.riskMonitoring =  TruffleContract({abi: data});
      App.riskMonitoring.setProvider(App.web3Provider);
    })
    return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-calRisk', App.handleCalRisk);
    $(document).on('click', '.btn-getRisk', App.handleGetRisk);
    $(document).on('click', '.btn-getVersion', App.handleVersion);
    $(document).on('click', '.btn-getAddUsdt', App.handleAddUsdt);
    $(document).on('click', '.btn-getNewAdd', App.handleNewAdd);
    $(document).on('click', '.btn-getTotalUsdt', App.handleTotalUsdt);
    $(document).on('click', '.btn-getTotalETH', App.handleTotalETH);
    $(document).on('click', '.btn-getReserveUsdt', App.handleReserveUSDT);
  },

  /* Calculate risk factor*/
  handleCalRisk: function(event) {

    event.preventDefault();

    web3.eth.getAccounts(function(err, accounts) {
      if(err) {
        console.log(error);
      }

      var account = accounts[0];
      var riskMonitoringInstance;

      App.riskMonitoring.at("0x93d27aaFf3cde3640A00761FFAC12e1FC20360eE").then(function(instance) {
        riskMonitoringInstance = instance;
        return riskMonitoringInstance.calcRiskFactor({from: account});
      }).then(function(res) {
        layer.msg('Success', {
          icon: 6,
          offset: '70px'
        });
        }).catch(function(err) {
          console.log(err.message);
        })
      });
  },
  /* Get risk factor */
  handleGetRisk: function(event) {

    event.preventDefault();

    web3.eth.getAccounts(function(err, accounts) {
      if(err) {
        console.log(error);
      }

      var account = accounts[0];
      var riskMonitoringInstance;

      App.riskMonitoring.at("0x93d27aaFf3cde3640A00761FFAC12e1FC20360eE").then(function(instance) {
        riskMonitoringInstance = instance;

        return riskMonitoringInstance.getRiskFactor.call();
      }).then(function(res) {
          $("#data-risk").text("Current risk factor:"+ res/10000);
        }).catch(function(err) {
          console.log(err.message);
        })
      });
  },
  /* Get version number */
  handleVersion: function(event) {
    var versionNum;
    $.ajax({
      url: 'http://101.35.24.15:9527/version',
      data:{"version":""},
      dataType: 'json',
      type: 'GET',
      success: function(data){
        versionNum = data["version"];
        $("#data-version").text("Version No.: "+versionNum);
      }
    });
    event.preventDefault();
  },
  /* Get the number of additional usdt */
  handleAddUsdt: function(event) {
    layui.use('table', function() {
      var table = layui.table;
      table.render({
        elem: '#getAddUsdt'
        , url: 'http://101.35.24.15:9527/getIssueEventsPoll'
        , parseData: function(res){
          tableData = res["events"];
          return {
            "code": 0,
            "count": tableData.length,
            "data": tableData
          };
        }
        , toolbar: true
        , title: "Detailed table of the number of additional usdt"
        , skin: 'line'
        , even: true
        , cols: [[
          {field: 'amount', title: 'The Number of Additional issues', width: 250, align: "center", sort: true}
          , {field: 'blockNumber', title: 'Block number', sort: true, width: 150}
          , {field: 'address', title: 'Contract Address'}
        ],]
      });
    });
    event.preventDefault();
  },
  /* Get the latest number of additional usdt issues */
  handleNewAdd: function(event) {
    $.ajax({
      url: 'http://101.35.24.15:9527/getIssueEventsPollCon',
      data:{"events":""},
      dataType: 'json',
      type: 'GET',
      success: function(data){
        events = JSON.stringify(data["events"]);
        $("#data-addition").text("Number of additional issues: "+events);
      }
    });
    event.preventDefault();
  },
  /* Get the total market cap of USDT outstanding */
  handleTotalUsdt: function (event){
    $.ajax({
      url: 'http://101.35.24.15:9527/getUSDTMKTCAP',
      data:{"MKTCAP":""},
      dataType: 'json',
      type: 'GET',
      success: function(data){
        number = JSON.stringify(data["MKTCAP"]);
        $("#data-totalUsdt").text("Total market cap(Usdt): "+ number);
      }
    });
  },
  /* Get the total market cap of ETH outstanding */
  handleTotalETH: function (event){
    $.ajax({
      url: 'http://101.35.24.15:9527/getETHMKTCAP',
      data:{"MKTCAP":""},
      dataType: 'json',
      type: 'GET',
      success: function(data){
        console.log(1);
        number = JSON.stringify(data["MKTCAP"]);
        $("#data-totalEth").text("Total market cap(Eth): "+ number);
      }
    });
  },
  /* Get USDT reserve amount */
  handleReserveUSDT: function (event){
    $.ajax({
      url: 'http://101.35.24.15:9527/getReserve',
      data:{"MKTCAP":""},
      dataType: 'json',
      type: 'GET',
      success: function(data){
        number = JSON.stringify(data["MKTCAP"]);
        $("#data-reserveUsdt").text("Get Usdt reserve amount: "+ number);
      }
    });
  }
};

// Initialize app when window loaded
$(function() {
  $(window).load(function() {
    App.init();
  });
});