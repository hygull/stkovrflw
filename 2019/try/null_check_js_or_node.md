```javascript
> a = undefined
undefined
> a = null
null
> a = 0
0
> a = undefined
undefined
> b = null
null
> c = 0
0
> 
> function f(v) {
... console.log(v)
... if(v) {
..... console.log('okay')
..... } else {
..... console.log('okay 2')
..... }}
undefined
> f(a)
undefined
okay 2
undefined
> f(b)
null
okay 2
undefined
> f(c)
0
okay 2
undefined
> f(1)
1
okay
undefined
> f('')

okay 2
undefined
> f(NaN)
NaN
okay 2
undefined
> f(Infinity)
Infinity
okay
undefined
> f(-Infinity)
-Infinity
okay
undefined
> 
```