### Checking type of varibale in JavaScript

```javascript
Last login: Wed Jun  5 16:25:52 on ttys002
no%                                                                                      ➜  src git:(master) ✗ node
> o = {}
{}
> p = null
null
> 
> type null
Thrown:
type null
     ^^^^

SyntaxError: Unexpected token null
> 
> typeof null
'object'
> 
> typeof []
'object'
> 
> Object.prototype.toString.call({})
'[object Object]'
> 
> Object.prototype.toString.call([])
'[object Array]'
> Object.prototype.toString.call([]).slice(8, -1)
'Array'
> 
> Object.prototype.toString.call(null).slice(8, -1)
'Null'
> Object.prototype.toString.call(undefined).slice(8, -1)
'Undefined'
> 
> Object.prototype.toString.call(89).slice(8, -1)
'Number'
> Object.prototype.toString.call(43.67).slice(8, -1)
'Number'
> Object.prototype.toString.call(true).slice(8, -1)
'Boolean'
> Object.prototype.toString.call('rishi').slice(8, -1)
'String'
> 
```