C/C++ swap a,b without extra variable小Trick：
```
auto a, b;
a = a + b;
b = a - b;
a = a - b;
```

In c++, size of a vector is unsigned long. We cannot use min(unsigned long, int);
That`s why we often int n = v.size();
