def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = []
    for i in range(4):
        if binary_str[::-1][i:i+1] == '1':
            handshake.append(actions[i])
    if binary_str[0] == '1':
        handshake.reverse()
    return handshake
