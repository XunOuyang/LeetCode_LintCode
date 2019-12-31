class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
    
private:
    void mergeSort(vector<int>& nums, int left, int right)
    {
        if(left < right)
        {
            int m = (right-left)/2+left;
            mergeSort(nums, left, m);
            mergeSort(nums, m+1, right);
            merge(nums, left, m, right);
        }
    }
    
    void merge(vector<int>& nums, int left, int mid, int right)
    {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        int L[n1], R[n2];
        for(int i=0; i<n1; i++)
        {
            L[i] = nums[left+i];
        }
        for(int i=0; i<n2; i++)
        {
            R[i] = nums[mid+1+i];
        }
        int i = 0;
        int j = 0;
        int k = 0;
        while(i < n1 && j < n2)
        {
            if(L[i] < R[j])
            {
                nums[k] = L[i];
                i++;
                k++;
            }
            else
            {
                nums[k] = R[j];
                j++;
                k++;
            }
        }
        while(i < n1)
        {
            nums[k] = L[i];
            i++;
            k++;
        }
        while(j < n2)
        {
            nums[k] = R[j];
            j++;
            k++;
        }
    }
};
