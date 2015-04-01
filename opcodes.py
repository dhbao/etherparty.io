opcodes = {
    'STOP':0,
    'ADD':1,
    'MUL':1,
    'SUB':1,
    'DIV':1,
    'SDIV':1,
    'MOD':1,
    'SMOD':1,
    'EXP':1,
    'NEG':1,
    'LT':1,
    'GT':1,
    'SLT':1,
    'SGT':1,
    'EQ':1,
    'NOT':1,
    'AND':1,
    'OR':1,
    'XOR':1,
    'BYTE':1,
    'ADDMOD':1,
    'MULMOD':1,
    'SHA3':20,
    'ADDRESS':1,
    'BALANCE':20,
    'ORIGIN':1,
    'CALLER':1,
    'CALLVALUE':1,
    'CALLDATALOAD':1,
    'CALLDATASIZE':1,
    'CALLDATACOPY':1,
    'CODESIZE':1,
    'CODECOPY':1,
    'GASPRICE':1,
    'PREVHASH':1,
    'TIMESTAMP':1,
    'NUMBER':1,
    'DIFFICULTY':1,
    'POP':1,
    'MLOAD':1,
    'MSTORE':1,
    'MSTORE8':1,
    'SLOAD':20,
    'SSTORE':0,
    'JUMP':1,
    'JUMPI':1,
    'PC':1,
    'MSIZE':1,
    'GAS':1,
    'CREATE':100,
    'CALL':20,
    'RETURN':1,
    'POST':20,
    'CALL_STATELESS':20,
    'ASSET_BALANCE':20,
    'SEND':20,
    'SUICIDE':0,
}

for i in range(1, 33):
    opcodes['PUSH' + str(i)] = 1
for i in range(1, 17):
    opcodes['DUP' + str(i)] = 1
    opcodes['SWAP' + str(i)] = 1