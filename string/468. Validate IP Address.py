class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            return self.IPv4(IP)
        return self.IPv6(IP)
        
    def IPv4(self, IP):
        IP = IP.split(".")
        if len(IP) != 4:
            return "Neither"
        for item in IP:
            try:
                if 0 <= int(item) < 256 and item == str(int(item)):
                    continue
                else:
                    return "Neither"
            except:
                return "Neither"
        return "IPv4"
    
    def IPv6(self, IP):
        IP = IP.split(":")
        if len(IP) != 8:
            return "Neither"
        for item in IP:
            if len(item) > 4 or len(item) < 1:
                return "Neither"
            elif any(not ("0" <= c <= "9" or "A" <= c <= "F" or "a" <= c <= "f") for c in item):
                return "Neither"
        return "IPv6"
