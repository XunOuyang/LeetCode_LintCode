// For this problem, we need to figure out what is expected fast, 
// in the meantime, we don`t necessarily need to convert all the numbers to octave, 
// just making use of the easy math will be enough.
// We also need to understand, that the sequence will contain more than 1 data string.
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int count = 0;
        for(int byte:data)
        {
            if(byte < 192 && byte >= 128)
            {
                if(count)
                    count -= 1;
                else
                    return false;
            }
            else if(count)
                return false;
            else if(byte < 128)
                continue;
            else if(byte < 224)
                count = 1;
            else if(byte < 240)
                count = 2;
            else if(byte < 248)
                count = 3;
            else
                return false;
        }
        return count == 0;
    }
};
