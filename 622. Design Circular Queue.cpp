// 这就是amazon 自己面试的时候挂了的题。

class MyCircularQueue {
public:
    int *arr;
    int start = 0;
    int end = 0;
    int size = 0;
    int capacity = 0;
    MyCircularQueue(int k) {
        arr = new int[k];
        size = k;
        for(int i=0; i < k; i++) {
            arr[i] = -1;
        }
    }
    
    bool enQueue(int value) {
        if(!isFull()) {
            arr[end] = value;
            end = (end + 1) % size;
            capacity += 1;
            return true;
        }
        return false;
    }
    
    bool deQueue() {
        if(!isEmpty()) {
            capacity -= 1;
            arr[start] = -1;
            if(start + 1 == size)
                start = 0;
            else 
                start++;
            return true;
        }
        return false;
    }
    
    int Front() {
        return arr[start];
    }
    
    int Rear() {
        return arr[(end + size - 1) % size];
    }
    
    bool isEmpty() {
        if(capacity == 0)
            return true;
        return false;
    }
    
    bool isFull() {
        if(capacity == size)
            return true;
        return false;
    }
};
