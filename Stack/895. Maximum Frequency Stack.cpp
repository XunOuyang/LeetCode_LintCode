class FreqStack {
public:    
    unordered_map<int, stack<int>> m;
    unordered_map<int, int> freq;
    int max_freq = 0;
    FreqStack() {
    }
    
    void push(int x) {
        if(freq.find(x) == freq.end() || freq[x] == 0)
        {
            freq[x] = 1;
        }
        else
        {
            freq[x] += 1;
        }
        m[freq[x]].push(x);
        max_freq = max(max_freq, freq[x]);
    }
    
    int pop() {
        int temp = m[max_freq].top();
        m[max_freq].pop();
        freq[temp] -= 1;
        if(m[max_freq].empty())
            max_freq -= 1;       
        return temp;
    }
};
