class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.emails_account_mapping = collections.defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                self.emails_account_mapping[account[j]].append(i)
        self.visited_accounts = [False] * len(accounts)
        for i, account in enumerate(accounts):
            if self.visited_accounts[i]:
                continue
            self.emails = set()
            self.dfs(i, accounts)
            print(self.emails)
            res.append([accounts[i][0]] + sorted(self.emails))
        return res
    
    def dfs(self, i, accounts):
        if self.visited_accounts[i]:
            return
        self.visited_accounts[i] = True
        account = accounts[i]
        for j in range(1, len(account)):
            self.emails.add(account[j])
            for item in self.emails_account_mapping[account[j]]:
                if not self.visited_accounts[item]:
                    self.dfs(item, accounts)
        
                
                
