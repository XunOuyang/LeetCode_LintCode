C/C++ swap a,b without extra variable小Trick：
```
auto a, b;
a = a + b;
b = a - b;
a = a - b;
```
