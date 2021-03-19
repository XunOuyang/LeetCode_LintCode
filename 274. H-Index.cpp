class Solution1 {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int h_index = citations.size();
        for(int i=0; i < citations.size(); i++)
        {
            if(citations[i] >= h_index)
                return h_index;
            else
                h_index--;
        }
        return 0;
    }
};

class Solution2 {
public:
    int hIndex(vector<int>& citations) {
        vector<int> paper(citations.size() + 1, 0);
        for(int& citation:citations)
        {
            if(citation >= citations.size())
                paper[citations.size()] += 1;
            else
                paper[citation] += 1;
        }
        
        for(int i = paper.size() - 1; i >= 1; i--)
        {
            paper[i-1] += paper[i];
            if(paper[i] >= i)
                return i;            
        }
        return 0;
    }
};
