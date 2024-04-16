def can_chain(dominoes):
    def dfs(chain):
        if not dominoes:
            return []
        if len(chain) == len(dominoes) and chain[0][0] == chain[-1][1]:
            return chain
        for i in range(len(dominoes)):
            if visited[i]:
                continue
            if not chain or chain[-1][1] == dominoes[i][0]:
                visited[i] = True
                result = dfs(chain + [dominoes[i]])
                if result:
                    return result
                visited[i] = False
            elif chain[-1][1] == dominoes[i][1]:
                visited[i] = True
                result = dfs(chain + [(dominoes[i][1], dominoes[i][0])])
                if result:
                    return result
                visited[i] = False
        return None

    visited = [False] * len(dominoes)
    return dfs([])