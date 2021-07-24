// https://stackoverflow.com/questions/68508020/javascript-classes-array-iteration/68508506#68508506
// Run: https://www.w3schools.com/code/tryit.asp?filename=GSS60TDWYWL8

// Make sure you have an element with id `app` in HTML body.
const div = document.getElementById('app'); 

class Arguments {
    constructor(title, img, depiction, price) {
        this.title = title
        this.img = img
        this.depiction = depiction
        this.price = price
    }
}

class Render {
    cards = [
        new Arguments('Python BootCamp', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7qKCjl9JJDnFDvf-U4Sv_YR5iXWGZbu-QRXNDZ5peS_Nusg8Sh8fb5lk5IbH9_MqSIIE&usqp=CAU', 'In this Complete Python course, you will learn everything you need to know about Python programming. You will start from very basics towards to the advance', 0.00,),
        new Arguments('JavaScript Crash Course', 'https://i.ytimg.com/vi/nN_qBdgmQpw/maxresdefault.jpg', 'A crach course by professional JS-DEVELOPER who"s wage $10000+', 300.00),new Arguments('JAVA COURSE', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvZ2DvlygW--TMKhrSO4SfA-6Op1QmVUXmh2dqtGxbHxPyvYH9elzpu-xGy2FOPac9VcE&usqp=CAU', 'A profi"s java totrial ', 70.00,),
    ]
    render() {
        const ul = document.createElement('ul')
        // const li = document.createElement('li');
        for (const elm of this.cards) {
                let li = document.createElement('li'); // Use the above commented line here     
                li.classList.add('card');  // Not -> li.classList.add = 'card'
                li.innerHTML = `<h1>${elm.title}</h1><img src='${elm.img}'><p>${elm.depiction}</p><h3>${elm.price}</h3>`
                ul.append(li)
            }
        div.append(ul)
    }
}

const Project = new Render(); // Instantiation
Project.render(); // Call render() method


/*
<!DOCTYPE html>
<html>
<body>

<span id="app"></span>

<script>
const div = document.getElementById('app')
class Arguments {
constructor(title, img, depiction, price) {
    this.title = title
    this.img = img
    this.depiction = depiction
    this.price = price
}
}

class Render {
cards = [
    new Arguments('Python BootCamp', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7qKCjl9JJDnFDvf-U4Sv_YR5iXWGZbu-QRXNDZ5peS_Nusg8Sh8fb5lk5IbH9_MqSIIE&usqp=CAU', 'In this Complete Python course, you will learn everything you need to know about Python programming. You will start from very basics towards to the advance', 0.00,),
    new Arguments('JavaScript Crash Course', 'https://i.ytimg.com/vi/nN_qBdgmQpw/maxresdefault.jpg', 'A crach course by professional JS-DEVELOPER who"s wage $10000+', 300.00),new Arguments('JAVA COURSE', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvZ2DvlygW--TMKhrSO4SfA-6Op1QmVUXmh2dqtGxbHxPyvYH9elzpu-xGy2FOPac9VcE&usqp=CAU', 'A profi"s java totrial ', 70.00,),
]
render() {
    const ul = document.createElement('ul')
    for (const elm of this.cards) {
            let li = document.createElement('li')       
            li.classList.add('card');  // Not -> li.classList.add = 'card'
            li.innerHTML = `<h1>${elm.title}</h1><img src='${elm.img}'><p>${elm.depiction}</p><h3>${elm.price}</h3>`
            ul.append(li)
        }
    div.append(ul)
}
}
const Project = new Render()
Project.render()
</script>

</body>
</html>
*/