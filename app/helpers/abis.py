TOKEN_ABI = [
    {"inputs":[{"internalType":"address","name":"_lzEndpoint","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":False,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":False,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":False,"internalType":"bytes32","name":"_hash","type":"bytes32"}],"name":"CallOFTReceivedSuccess","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":False,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":False,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":False,"internalType":"bytes","name":"_payload","type":"bytes"},{"indexed":False,"internalType":"bytes","name":"_reason","type":"bytes"}],"name":"MessageFailed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"_address","type":"address"}],"name":"NonContractAddress","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":True,"internalType":"address","name":"_to","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"ReceiveFromChain","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":False,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":False,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":False,"internalType":"bytes32","name":"_payloadHash","type":"bytes32"}],"name":"RetryMessageSuccess","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":True,"internalType":"address","name":"_from","type":"address"},{"indexed":True,"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"SendToChain","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"feeBp","type":"uint16"}],"name":"SetDefaultFeeBp","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"dstchainId","type":"uint16"},{"indexed":False,"internalType":"bool","name":"enabled","type":"bool"},{"indexed":False,"internalType":"uint16","name":"feeBp","type":"uint16"}],"name":"SetFeeBp","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeOwner","type":"address"}],"name":"SetFeeOwner","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":False,"internalType":"uint16","name":"_type","type":"uint16"},{"indexed":False,"internalType":"uint256","name":"_minDstGas","type":"uint256"}],"name":"SetMinDstGas","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"precrime","type":"address"}],"name":"SetPrecrime","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":False,"internalType":"bytes","name":"_path","type":"bytes"}],"name":"SetTrustedRemote","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":False,"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"SetTrustedRemoteAddress","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bool","name":"_useCustomAdapterParams","type":"bool"}],"name":"SetUseCustomAdapterParams","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"BP_DENOMINATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"NO_EXTRA_GAS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PT_SEND","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PT_SEND_AND_CALL","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes32","name":"_from","type":"bytes32"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_payload","type":"bytes"},{"internalType":"uint256","name":"_gasForCall","type":"uint256"}],"name":"callOnOFTReceived","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"chainIdToFeeBps","outputs":[{"internalType":"uint16","name":"feeBP","type":"uint16"},{"internalType":"bool","name":"enabled","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"circulatingSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"creditedPackets","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"defaultFeeBp","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_payload","type":"bytes"},{"internalType":"uint64","name":"_dstGasForCall","type":"uint64"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendAndCallFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"failedMessages","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"}],"name":"getTrustedRemoteAddress","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"isTrustedRemote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"}],"name":"minDstGasLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"nonblockingLzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"precrime","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"quoteOFTFee","outputs":[{"internalType":"uint256","name":"fee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"retryMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_minAmount","type":"uint256"},{"internalType":"bytes","name":"_payload","type":"bytes"},{"internalType":"uint64","name":"_dstGasForCall","type":"uint64"},{"components":[{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"adapterParams","type":"bytes"}],"internalType":"struct ICommonOFT.LzCallParams","name":"_callParams","type":"tuple"}],"name":"sendAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes32","name":"_toAddress","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_minAmount","type":"uint256"},{"components":[{"internalType":"address payable","name":"refundAddress","type":"address"},{"internalType":"address","name":"zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"adapterParams","type":"bytes"}],"internalType":"struct ICommonOFT.LzCallParams","name":"_callParams","type":"tuple"}],"name":"sendFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_feeBp","type":"uint16"}],"name":"setDefaultFeeBp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bool","name":"_enabled","type":"bool"},{"internalType":"uint16","name":"_feeBp","type":"uint16"}],"name":"setFeeBp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeOwner","type":"address"}],"name":"setFeeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint16","name":"_packetType","type":"uint16"},{"internalType":"uint256","name":"_minGas","type":"uint256"}],"name":"setMinDstGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_precrime","type":"address"}],"name":"setPrecrime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_path","type":"bytes"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setTrustedRemoteAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_useCustomAdapterParams","type":"bool"}],"name":"setUseCustomAdapterParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"sharedDecimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"trustedRemoteLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"useCustomAdapterParams","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]

JOE_ROUTER_ABI = [
    {
        "inputs": [
            {
                "internalType": "contract ILBFactory",
                "name": "factory",
                "type": "address"
            },
            {
                "internalType": "contract IJoeFactory",
                "name": "factoryV1",
                "type": "address"
            },
            {
                "internalType": "contract ILBLegacyFactory",
                "name": "legacyFactory",
                "type": "address"
            },
            {
                "internalType": "contract ILBLegacyRouter",
                "name": "legacyRouter",
                "type": "address"
            },
            {
                "internalType": "contract IWNATIVE",
                "name": "wnative",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "AddressHelper__CallFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "AddressHelper__NonContract",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "JoeLibrary__InsufficientAmount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "JoeLibrary__InsufficientLiquidity",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountSlippage",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__AmountSlippageBPTooBig",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountXMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountX",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountY",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__AmountSlippageCaught",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__BinReserveOverflows",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LBRouter__BrokenSwapSafetyCheck",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "currentTimestamp",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__DeadlineExceeded",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__FailedToSendNATIVE",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "idDesired",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "idSlippage",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__IdDesiredOverflows",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "int256",
                "name": "id",
                "type": "int256"
            }
        ],
        "name": "LBRouter__IdOverflows",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "activeIdDesired",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "idSlippage",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "activeId",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__IdSlippageCaught",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__InsufficientAmountOut",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "wrongToken",
                "type": "address"
            }
        ],
        "name": "LBRouter__InvalidTokenPath",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "version",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__InvalidVersion",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LBRouter__LengthsMismatch",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountInMax",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__MaxAmountInExceeded",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LBRouter__NotFactoryOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenX",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenY",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "binStep",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__PairNotCreated",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LBRouter__SenderIsNotWNATIVE",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__SwapOverflows",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "excess",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__TooMuchTokensIn",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "reserve",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__WrongAmounts",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenX",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenY",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amountX",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountY",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "msgValue",
                "type": "uint256"
            }
        ],
        "name": "LBRouter__WrongNativeLiquidityParameters",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LBRouter__WrongTokenOrder",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TokenHelper__TransferFailed",
        "type": "error"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "contract IERC20",
                        "name": "tokenX",
                        "type": "address"
                    },
                    {
                        "internalType": "contract IERC20",
                        "name": "tokenY",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "binStep",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountX",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountY",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountXMin",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountYMin",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "activeIdDesired",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "idSlippage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "int256[]",
                        "name": "deltaIds",
                        "type": "int256[]"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "distributionX",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "distributionY",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "address",
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "refundTo",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deadline",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct ILBRouter.LiquidityParameters",
                "name": "liquidityParameters",
                "type": "tuple"
            }
        ],
        "name": "addLiquidity",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountXAdded",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYAdded",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountXLeft",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYLeft",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "depositIds",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityMinted",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "contract IERC20",
                        "name": "tokenX",
                        "type": "address"
                    },
                    {
                        "internalType": "contract IERC20",
                        "name": "tokenY",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "binStep",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountX",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountY",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountXMin",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountYMin",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "activeIdDesired",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "idSlippage",
                        "type": "uint256"
                    },
                    {
                        "internalType": "int256[]",
                        "name": "deltaIds",
                        "type": "int256[]"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "distributionX",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "distributionY",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "address",
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "refundTo",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "deadline",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct ILBRouter.LiquidityParameters",
                "name": "liquidityParameters",
                "type": "tuple"
            }
        ],
        "name": "addLiquidityNATIVE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountXAdded",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYAdded",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountXLeft",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYLeft",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "depositIds",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityMinted",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "tokenX",
                "type": "address"
            },
            {
                "internalType": "contract IERC20",
                "name": "tokenY",
                "type": "address"
            },
            {
                "internalType": "uint24",
                "name": "activeId",
                "type": "uint24"
            },
            {
                "internalType": "uint16",
                "name": "binStep",
                "type": "uint16"
            }
        ],
        "name": "createLBPair",
        "outputs": [
            {
                "internalType": "contract ILBPair",
                "name": "pair",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getFactory",
        "outputs": [
            {
                "internalType": "contract ILBFactory",
                "name": "lbFactory",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILBPair",
                "name": "pair",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "price",
                "type": "uint256"
            }
        ],
        "name": "getIdFromPrice",
        "outputs": [
            {
                "internalType": "uint24",
                "name": "",
                "type": "uint24"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getLegacyFactory",
        "outputs": [
            {
                "internalType": "contract ILBLegacyFactory",
                "name": "legacyLBfactory",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getLegacyRouter",
        "outputs": [
            {
                "internalType": "contract ILBLegacyRouter",
                "name": "legacyRouter",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILBPair",
                "name": "pair",
                "type": "address"
            },
            {
                "internalType": "uint24",
                "name": "id",
                "type": "uint24"
            }
        ],
        "name": "getPriceFromId",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILBPair",
                "name": "pair",
                "type": "address"
            },
            {
                "internalType": "uint128",
                "name": "amountOut",
                "type": "uint128"
            },
            {
                "internalType": "bool",
                "name": "swapForY",
                "type": "bool"
            }
        ],
        "name": "getSwapIn",
        "outputs": [
            {
                "internalType": "uint128",
                "name": "amountIn",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "amountOutLeft",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "fee",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILBPair",
                "name": "pair",
                "type": "address"
            },
            {
                "internalType": "uint128",
                "name": "amountIn",
                "type": "uint128"
            },
            {
                "internalType": "bool",
                "name": "swapForY",
                "type": "bool"
            }
        ],
        "name": "getSwapOut",
        "outputs": [
            {
                "internalType": "uint128",
                "name": "amountInLeft",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "amountOut",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "fee",
                "type": "uint128"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getV1Factory",
        "outputs": [
            {
                "internalType": "contract IJoeFactory",
                "name": "factoryV1",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getWNATIVE",
        "outputs": [
            {
                "internalType": "contract IWNATIVE",
                "name": "wnative",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "tokenX",
                "type": "address"
            },
            {
                "internalType": "contract IERC20",
                "name": "tokenY",
                "type": "address"
            },
            {
                "internalType": "uint16",
                "name": "binStep",
                "type": "uint16"
            },
            {
                "internalType": "uint256",
                "name": "amountXMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountYMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidity",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountX",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountY",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "token",
                "type": "address"
            },
            {
                "internalType": "uint16",
                "name": "binStep",
                "type": "uint16"
            },
            {
                "internalType": "uint256",
                "name": "amountTokenMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountNATIVEMin",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address payable",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidityNATIVE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountToken",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountNATIVE",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactNATIVEForTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactNATIVEForTokensSupportingFeeOnTransferTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOutMinNATIVE",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address payable",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactTokensForNATIVE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOutMinNATIVE",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address payable",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactTokensForNATIVESupportingFeeOnTransferTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapNATIVEForExactTokens",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "amountsIn",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountNATIVEOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountInMax",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address payable",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapTokensForExactNATIVE",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "amountsIn",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountInMax",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256[]",
                        "name": "pairBinSteps",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "enum ILBRouter.Version[]",
                        "name": "versions",
                        "type": "uint8[]"
                    },
                    {
                        "internalType": "contract IERC20[]",
                        "name": "tokenPath",
                        "type": "address[]"
                    }
                ],
                "internalType": "struct ILBRouter.Path",
                "name": "path",
                "type": "tuple"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapTokensForExactTokens",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "amountsIn",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "token",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "sweep",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ILBToken",
                "name": "lbToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "sweepLBToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]

