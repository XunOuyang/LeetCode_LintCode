class Solution {
public:    
    vector<string> letterCasePermutation(string S) {
        vector<string> res{S};
        for(int i=0; i<S.size(); i++) {
            vector<string> new_res;
            vector<string>::iterator it;
            for(it = res.begin(); it != res.end(); it++) {
                if(isalpha((*it)[i])){
                    new_res.push_back((*it).substr(0, i)+char(tolower((*it)[i]))+(*it).substr(i+1, S.size()));   
                    new_res.push_back((*it).substr(0, i)+char(toupper((*it)[i]))+(*it).substr(i+1, S.size())); 
                }
                else
                    new_res.push_back(*it);
            }
            res = new_res;
        }
        return res;
    }
};