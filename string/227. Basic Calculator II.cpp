class Solution {
public:
    int calculate(string s) {
        if(s.size() == 0)
            return 0;
        stack<char> operations;
        stack<int> values;
        string temp = "";
        for(char& c:s)
        {
            if(c == ' ')
                continue;
            if(isdigit(c))
                temp += c;
            else
            {
                if(temp != "")
                {
                    values.push(stoi(temp));
                    temp = "";
                }
                while(!operations.empty() && (operations.top() == '*' || operations.top() == '/' || c == '+' || c == '-'))
                {
                    operate(values, operations);
                }       
                operations.push(c);
            }
        }
        values.push(stoi(temp));
        while(!operations.empty())
            operate(values, operations);
        return values.top();
    }
    
    void operate(stack<int>& values, stack<char>& operations)
    {
        int a = values.top();
        values.pop();
        if(operations.top() == '+')
        {
            values.top() += a;
        }
        else if(operations.top() == '-')
        {
            values.top() -= a;
        }
        else if(operations.top() == '*')
        {
            values.top() *= a;
        }
        else if(operations.top() == '/')
        {
            values.top() /= a;
        }
        operations.pop();
    }
};
