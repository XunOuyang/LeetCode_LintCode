# Insertion sort:
It has the same time complexity as Bubble sort. The difference is, the first element is considered to be the sorted one. We take start to take the element from the second one to compare with all the elements which are ahead of the second one, if the second one is greater than that, then it find it spot, if not, it will be moved to forward. See the GIF below:

<img src="image/Insertion-sort-example-300px.gif" width="400" height="248" />


# Quick Sort:
```
int partition(int arr[], int lo, int hi)
{
    int pivot = arr[hi];
    int i = lo;
    for(int j=lo; j < hi; j++)
    {
        if(arr[j] < pivot)
        {
            std::swap(arr[i], arr[j]);
            i++;
        }
    }
    std::swap(arr[i], arr[hi]);
    return i;
}

int quicksort(int arr[], int lo, int hi)
{
    int p = partition(arr, lo, hi);
    quicksort(arr, low, p - 1);
    quicksort(arr, p + 1, hi);
}

int main()
{
    int a[] = {5,3,7,1,9,2,4,8,6};
    quicksort(a, 0, sizeof(a)/sizeof(a[0]) - 1);
    for(int i=0; i < 9; i++)
    {
        std::cout << a[i] << std::endl;
    }
    return 1;
}
```

### Merge Sort: 148
