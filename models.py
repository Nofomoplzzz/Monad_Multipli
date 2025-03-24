class AbIs:
    sepolia = [{"inputs": [{"internalType": "string", "name": "_name", "type": "string"},
                           {"internalType": "string", "name": "_symbol", "type": "string"},
                           {"internalType": "address", "name": "_lzEndpoint", "type": "address"},
                           {"internalType": "uint256", "name": "_minSendAmount", "type": "uint256"}],
                "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "spender", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval",
                                                                          "type": "event"}, {"anonymous": False,
                                                                                             "inputs": [
                                                                                                 {"indexed": True,
                                                                                                  "internalType": "address",
                                                                                                  "name": "_dst",
                                                                                                  "type": "address"},
                                                                                                 {"indexed": False,
                                                                                                  "internalType": "uint256",
                                                                                                  "name": "_amount",
                                                                                                  "type": "uint256"}],
                                                                                             "name": "Deposit",
                                                                                             "type": "event"},
               {"anonymous": False,
                "inputs": [{"indexed": False, "internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                           {"indexed": False, "internalType": "bytes", "name": "_srcAddress", "type": "bytes"},
                           {"indexed": False, "internalType": "uint64", "name": "_nonce", "type": "uint64"},
                           {"indexed": False, "internalType": "bytes", "name": "_payload", "type": "bytes"},
                           {"indexed": False, "internalType": "bytes", "name": "_reason", "type": "bytes"}],
                "name": "MessageFailed", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}],
                                                            "name": "OwnershipTransferred", "type": "event"},
               {"anonymous": False,
                "inputs": [{"indexed": True, "internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                           {"indexed": True, "internalType": "address", "name": "_to", "type": "address"},
                           {"indexed": False, "internalType": "uint256", "name": "_amount", "type": "uint256"}],
                "name": "ReceiveFromChain", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": False, "internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
            {"indexed": False, "internalType": "bytes", "name": "_srcAddress", "type": "bytes"},
            {"indexed": False, "internalType": "uint64", "name": "_nonce", "type": "uint64"},
            {"indexed": False, "internalType": "bytes32", "name": "_payloadHash", "type": "bytes32"}],
                                                               "name": "RetryMessageSuccess", "type": "event"},
               {"anonymous": False,
                "inputs": [{"indexed": True, "internalType": "uint16", "name": "_dstChainId", "type": "uint16"},
                           {"indexed": True, "internalType": "address", "name": "_from", "type": "address"},
                           {"indexed": False, "internalType": "bytes", "name": "_toAddress", "type": "bytes"},
                           {"indexed": False, "internalType": "uint256", "name": "_amount", "type": "uint256"}],
                "name": "SendToChain", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": False, "internalType": "uint16", "name": "_dstChainId", "type": "uint16"},
            {"indexed": False, "internalType": "uint16", "name": "_type", "type": "uint16"},
            {"indexed": False, "internalType": "uint256", "name": "_minDstGas", "type": "uint256"}],
                                                          "name": "SetMinDstGas", "type": "event"}, {"anonymous": False,
                                                                                                     "inputs": [{
                                                                                                         "indexed": False,
                                                                                                         "internalType": "address",
                                                                                                         "name": "precrime",
                                                                                                         "type": "address"}],
                                                                                                     "name": "SetPrecrime",
                                                                                                     "type": "event"},
               {"anonymous": False,
                "inputs": [{"indexed": False, "internalType": "uint16", "name": "_remoteChainId", "type": "uint16"},
                           {"indexed": False, "internalType": "bytes", "name": "_path", "type": "bytes"}],
                "name": "SetTrustedRemote", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": False, "internalType": "uint16", "name": "_remoteChainId", "type": "uint16"},
            {"indexed": False, "internalType": "bytes", "name": "_remoteAddress", "type": "bytes"}],
                                                               "name": "SetTrustedRemoteAddress", "type": "event"},
               {"anonymous": False, "inputs": [
                   {"indexed": False, "internalType": "bool", "name": "_useCustomAdapterParams", "type": "bool"}],
                "name": "SetUseCustomAdapterParams", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer",
                                                                        "type": "event"}, {"anonymous": False,
                                                                                           "inputs": [{"indexed": True,
                                                                                                       "internalType": "address",
                                                                                                       "name": "_src",
                                                                                                       "type": "address"},
                                                                                                      {"indexed": False,
                                                                                                       "internalType": "uint256",
                                                                                                       "name": "_amount",
                                                                                                       "type": "uint256"}],
                                                                                           "name": "Withdrawal",
                                                                                           "type": "event"},
               {"inputs": [], "name": "NO_EXTRA_GAS",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                "type": "function"},
               {"inputs": [], "name": "PT_SEND", "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
                "stateMutability": "view", "type": "function"}, {
                   "inputs": [{"internalType": "address", "name": "owner", "type": "address"},
                              {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance",
                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                   "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"},
                                                    {"internalType": "uint256", "name": "amount", "type": "uint256"}],
                                         "name": "approve",
                                         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                                         "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "balanceOf",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                "type": "function"}, {"inputs": [], "name": "circulatingSupply",
                                      "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                      "stateMutability": "view", "type": "function"},
               {"inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
                "stateMutability": "view", "type": "function"}, {
                   "inputs": [{"internalType": "address", "name": "spender", "type": "address"},
                              {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}],
                   "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                   "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_dstChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_toAddress", "type": "bytes"},
                              {"internalType": "uint256", "name": "_amount", "type": "uint256"},
                              {"internalType": "bool", "name": "_useZro", "type": "bool"},
                              {"internalType": "bytes", "name": "_adapterParams", "type": "bytes"}],
                   "name": "estimateSendFee",
                   "outputs": [{"internalType": "uint256", "name": "nativeFee", "type": "uint256"},
                               {"internalType": "uint256", "name": "zroFee", "type": "uint256"}],
                   "stateMutability": "view", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "", "type": "uint16"},
                              {"internalType": "bytes", "name": "", "type": "bytes"},
                              {"internalType": "uint64", "name": "", "type": "uint64"}], "name": "failedMessages",
                   "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view",
                   "type": "function"}, {"inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                                                    {"internalType": "bytes", "name": "_srcAddress", "type": "bytes"}],
                                         "name": "forceResumeReceive", "outputs": [], "stateMutability": "nonpayable",
                                         "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_version", "type": "uint16"},
                              {"internalType": "uint16", "name": "_chainId", "type": "uint16"},
                              {"internalType": "address", "name": "", "type": "address"},
                              {"internalType": "uint256", "name": "_configType", "type": "uint256"}],
                   "name": "getConfig", "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
                   "stateMutability": "view", "type": "function"},
               {"inputs": [{"internalType": "uint16", "name": "_remoteChainId", "type": "uint16"}],
                "name": "getTrustedRemoteAddress", "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
                "stateMutability": "view", "type": "function"}, {
                   "inputs": [{"internalType": "address", "name": "spender", "type": "address"},
                              {"internalType": "uint256", "name": "addedValue", "type": "uint256"}],
                   "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                   "stateMutability": "nonpayable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_srcAddress", "type": "bytes"}],
                   "name": "isTrustedRemote", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                   "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "lzEndpoint", "outputs": [
            {"internalType": "contract ILayerZeroEndpoint", "name": "", "type": "address"}], "stateMutability": "view",
                                                                    "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_srcAddress", "type": "bytes"},
                              {"internalType": "uint64", "name": "_nonce", "type": "uint64"},
                              {"internalType": "bytes", "name": "_payload", "type": "bytes"}], "name": "lzReceive",
                   "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "", "type": "uint16"},
                              {"internalType": "uint16", "name": "", "type": "uint16"}], "name": "minDstGasLookup",
                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                   "type": "function"}, {"inputs": [], "name": "minSendAmount",
                                         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                         "stateMutability": "view", "type": "function"},
               {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                "stateMutability": "view", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_srcAddress", "type": "bytes"},
                              {"internalType": "uint64", "name": "_nonce", "type": "uint64"},
                              {"internalType": "bytes", "name": "_payload", "type": "bytes"}],
                   "name": "nonblockingLzReceive", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "precrime", "outputs": [
            {"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
               {"inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable",
                "type": "function"}, {"inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                                                 {"internalType": "bytes", "name": "_srcAddress", "type": "bytes"},
                                                 {"internalType": "uint64", "name": "_nonce", "type": "uint64"},
                                                 {"internalType": "bytes", "name": "_payload", "type": "bytes"}],
                                      "name": "retryMessage", "outputs": [], "stateMutability": "payable",
                                      "type": "function"}, {
                   "inputs": [{"internalType": "address", "name": "_from", "type": "address"},
                              {"internalType": "uint16", "name": "_dstChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_toAddress", "type": "bytes"},
                              {"internalType": "uint256", "name": "_amount", "type": "uint256"},
                              {"internalType": "address payable", "name": "_refundAddress", "type": "address"},
                              {"internalType": "address", "name": "_zroPaymentAddress", "type": "address"},
                              {"internalType": "bytes", "name": "_adapterParams", "type": "bytes"}], "name": "sendFrom",
                   "outputs": [], "stateMutability": "payable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_version", "type": "uint16"},
                              {"internalType": "uint16", "name": "_chainId", "type": "uint16"},
                              {"internalType": "uint256", "name": "_configType", "type": "uint256"},
                              {"internalType": "bytes", "name": "_config", "type": "bytes"}], "name": "setConfig",
                   "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_dstChainId", "type": "uint16"},
                              {"internalType": "uint16", "name": "_packetType", "type": "uint16"},
                              {"internalType": "uint256", "name": "_minGas", "type": "uint256"}],
                   "name": "setMinDstGas", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "uint256", "name": "_minSendAmount", "type": "uint256"}],
                "name": "setMinSendAmount", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "address", "name": "_precrime", "type": "address"}], "name": "setPrecrime",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "uint16", "name": "_version", "type": "uint16"}],
                "name": "setReceiveVersion", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "uint16", "name": "_version", "type": "uint16"}], "name": "setSendVersion",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_srcChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_path", "type": "bytes"}], "name": "setTrustedRemote",
                   "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                   "inputs": [{"internalType": "uint16", "name": "_remoteChainId", "type": "uint16"},
                              {"internalType": "bytes", "name": "_remoteAddress", "type": "bytes"}],
                   "name": "setTrustedRemoteAddress", "outputs": [], "stateMutability": "nonpayable",
                   "type": "function"},
               {"inputs": [{"internalType": "bool", "name": "_useCustomAdapterParams", "type": "bool"}],
                "name": "setUseCustomAdapterParams", "outputs": [], "stateMutability": "nonpayable",
                "type": "function"}, {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}],
                                      "name": "supportsInterface",
                                      "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                                      "stateMutability": "view", "type": "function"},
               {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                "stateMutability": "view", "type": "function"},
               {"inputs": [], "name": "token", "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalSupply", "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
               {"inputs": [{"internalType": "address", "name": "to", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer",
                "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable",
                "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"},
                                                 {"internalType": "address", "name": "to", "type": "address"},
                                                 {"internalType": "uint256", "name": "amount", "type": "uint256"}],
                                      "name": "transferFrom",
                                      "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                                      "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
                "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"inputs": [{"internalType": "uint16", "name": "", "type": "uint16"}], "name": "trustedRemoteLookup",
                "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}], "stateMutability": "view",
                "type": "function"}, {"inputs": [], "name": "useCustomAdapterParams",
                                      "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                                      "stateMutability": "view", "type": "function"},
               {"inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}], "name": "withdraw",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"},
               {"stateMutability": "payable", "type": "receive"}]

    bridge_sep_tomon = [
        {
            "inputs": [
                {
                    "name": "recipient",
                    "type": "address"
                },
                {
                    "name": "tokens",
                    "type": "address[]"
                },
                {
                    "name": "amounts",
                    "type": "uint256[]"
                }
            ],
            "name": "transferTokens",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]

    multipl = [{
        "constant": False,
        "inputs": [
            {
                "name": "recipient",
                "type": "address"
            }
        ],
        "name": "claimToken",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
        {
            "constant": False,
            "inputs": [
                {
                    "name": "recipient",
                    "type": "address"
                },
                {
                    "name": "amount",
                    "type": "uint256"
                }
            ],
            "name": "deposit",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },

        {
            "constant": False,
            "inputs": [
                {
                    "name": "spender",
                    "type": "address"
                },
                {
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "approve",
            "outputs": [
                {
                    "name": "",
                    "type": "bool"
                }
            ],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        }

    ]

    usdc = [
        {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False,
         "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [{"name": "_upgradedAddress", "type": "address"}], "name": "deprecate",
         "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}],
         "name": "approve", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [], "name": "deprecated", "outputs": [{"name": "", "type": "bool"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [{"name": "_evilUser", "type": "address"}], "name": "addBlackList", "outputs": [],
         "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [
            {"name": "_from", "type": "address"}, {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": False,
                                                                            "stateMutability": "nonpayable",
                                                                            "type": "function"},
        {"constant": True, "inputs": [], "name": "upgradedAddress", "outputs": [{"name": "", "type": "address"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "balances",
         "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "maximumFee", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "_totalSupply", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [], "name": "unpause", "outputs": [], "payable": False,
         "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [{"name": "_maker", "type": "address"}], "name": "getBlackListStatus",
         "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}],
         "name": "allowed", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view",
         "type": "function"},
        {"constant": True, "inputs": [], "name": "paused", "outputs": [{"name": "", "type": "bool"}], "payable": False,
         "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [{"name": "who", "type": "address"}], "name": "balanceOf",
         "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [], "name": "pause", "outputs": [], "payable": False,
         "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [], "name": "getOwner", "outputs": [{"name": "", "type": "address"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
         "name": "transfer", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": False,
         "inputs": [{"name": "newBasisPoints", "type": "uint256"}, {"name": "newMaxFee", "type": "uint256"}],
         "name": "setParams", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "issue", "outputs": [],
         "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "redeem", "outputs": [],
         "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}],
         "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": False,
         "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [], "name": "basisPointsRate", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "isBlackListed",
         "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [{"name": "_clearedUser", "type": "address"}], "name": "removeBlackList",
         "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": True, "inputs": [], "name": "MAX_UINT", "outputs": [{"name": "", "type": "uint256"}],
         "payable": False, "stateMutability": "view", "type": "function"},
        {"constant": False, "inputs": [{"name": "newOwner", "type": "address"}], "name": "transferOwnership",
         "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
        {"constant": False, "inputs": [{"name": "_blackListedUser", "type": "address"}], "name": "destroyBlackFunds",
         "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {
            "inputs": [{"name": "_initialSupply", "type": "uint256"}, {"name": "_name", "type": "string"},
                       {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint256"}],
            "payable": False, "stateMutability": "nonpayable", "type": "constructor"},
        {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Issue",
         "type": "event"},
        {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Redeem",
         "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "newAddress", "type": "address"}],
                            "name": "Deprecate", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": False, "name": "feeBasisPoints", "type": "uint256"},
            {"indexed": False, "name": "maxFee", "type": "uint256"}], "name": "Params", "type": "event"},
        {"anonymous": False, "inputs": [{"indexed": False, "name": "_blackListedUser", "type": "address"},
                                        {"indexed": False, "name": "_balance", "type": "uint256"}],
         "name": "DestroyedBlackFunds", "type": "event"},
        {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}],
         "name": "AddedBlackList", "type": "event"},
        {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}],
         "name": "RemovedBlackList", "type": "event"}, {"anonymous": False, "inputs": [
            {"indexed": True, "name": "owner", "type": "address"},
            {"indexed": True, "name": "spender", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"},
        {"anonymous": False, "inputs": [{"indexed": True, "name": "from", "type": "address"},
                                        {"indexed": True, "name": "to", "type": "address"},
                                        {"indexed": False, "name": "value", "type": "uint256"}], "name": "Transfer",
         "type": "event"}, {"anonymous": False, "inputs": [], "name": "Pause", "type": "event"},
        {"anonymous": False, "inputs": [], "name": "Unpause", "type": "event"}]


    wrap_monad = [{"anonymous": False,
                   "inputs": [{"indexed": True, "internalType": "address", "name": "src", "type": "address"},
                              {"indexed": True, "internalType": "address", "name": "guy", "type": "address"},
                              {"indexed": False, "internalType": "uint256", "name": "wad", "type": "uint256"}],
                   "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "dst", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "wad", "type": "uint256"}], "name": "Deposit",
                                                          "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "src", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "dst", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "wad", "type": "uint256"}], "name": "Transfer",
                                                                             "type": "event"}, {"anonymous": False,
                                                                                                "inputs": [
                                                                                                    {"indexed": True,
                                                                                                     "internalType": "address",
                                                                                                     "name": "src",
                                                                                                     "type": "address"},
                                                                                                    {"indexed": False,
                                                                                                     "internalType": "uint256",
                                                                                                     "name": "wad",
                                                                                                     "type": "uint256"}],
                                                                                                "name": "Withdrawal",
                                                                                                "type": "event"},
                  {"stateMutability": "payable", "type": "fallback"}, {
                      "inputs": [{"internalType": "address", "name": "", "type": "address"},
                                 {"internalType": "address", "name": "", "type": "address"}], "name": "allowance",
                      "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                      "stateMutability": "view", "type": "function"}, {
                      "inputs": [{"internalType": "address", "name": "guy", "type": "address"},
                                 {"internalType": "uint256", "name": "wad", "type": "uint256"}], "name": "approve",
                      "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                      "stateMutability": "nonpayable", "type": "function"},
                  {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "balanceOf",
                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                   "type": "function"}, {"inputs": [], "name": "decimals",
                                         "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
                                         "stateMutability": "view", "type": "function"},
                  {"inputs": [], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function"},
                  {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                   "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [
            {"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
                  {"inputs": [], "name": "totalSupply",
                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                   "type": "function"}, {"inputs": [{"internalType": "address", "name": "dst", "type": "address"},
                                                    {"internalType": "uint256", "name": "wad", "type": "uint256"}],
                                         "name": "transfer",
                                         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                                         "stateMutability": "nonpayable", "type": "function"}, {
                      "inputs": [{"internalType": "address", "name": "src", "type": "address"},
                                 {"internalType": "address", "name": "dst", "type": "address"},
                                 {"internalType": "uint256", "name": "wad", "type": "uint256"}], "name": "transferFrom",
                      "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                      "stateMutability": "nonpayable", "type": "function"},
                  {"inputs": [{"internalType": "uint256", "name": "wad", "type": "uint256"}], "name": "withdraw",
                   "outputs": [], "stateMutability": "nonpayable", "type": "function"}]

    bean = [
    {
        "constant": False,
        "inputs": [
            {
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "name": "path",
                "type": "address[]"
            },
            {
                "name": "to",
                "type": "address"
            },
            {
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactETHForTokens",
        "outputs": [
            {
                "name": "",
                "type": "uint256[]"
            }
        ],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },

        {
            "name": "addLiquidityETH",
            "type": "function",
            "inputs": [
                {
                    "name": "token",
                    "type": "address"
                },
                {
                    "name": "amountTokenDesired",
                    "type": "uint256"
                },
                {
                    "name": "amountTokenMin",
                    "type": "uint256"
                },
                {
                    "name": "amountETHMin",
                    "type": "uint256"
                },
                {
                    "name": "to",
                    "type": "address"
                },
                {
                    "name": "deadline",
                    "type": "uint256"
                }
            ],
            "outputs": [
                {
                    "name": "",
                    "type": "uint256"
                },
                {
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "payable"
        }

    ]
