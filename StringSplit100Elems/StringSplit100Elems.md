**@D.Lene**, according to the output provided in the question. I have written the below code which gives youur output.

> **Note:** Please do not forget to look at code executed on **Node REPL** after the below code. It will give you a clean understanding of each and every line.
>
> And leave comment if the below code does not satify your need by  provide more outputs (that you actuially need for some specific inputs) as I am not counting for 100 characters as your provided output array's elements are not exactly of length 100 (it's 80, 78, 81, ...) which is clear in **Node REPL** testing.
>
> If you are still looking for 100 characters then based on your provided data input(s) & output(s), I will need to change the code. 

    var data = "<:cmd:409342761179938838> " +
              "<:nobot:409342761246916610> " +
              "<:haha:409342761272344578> " +
              "<:rrrr:409342761431728139> " +
              "<:aaa:409342761439854593> " +
              "<:fff:409342761503031296> " +
              "<:woah:409342761532391424> " +
              "<:swon:409342761549037568> " +
              "<:owoah:409342761595043850> "+
              "<:sss:409342761662414848>"

    var arr = data.split(' ')
    console.log(arr)
    /*
      [ '<:cmd:409342761179938838>',
        '<:nobot:409342761246916610>',
        '<:haha:409342761272344578>',
        '<:rrrr:409342761431728139>',
        '<:aaa:409342761439854593>',
        '<:fff:409342761503031296>',
        '<:woah:409342761532391424>',
        '<:swon:409342761549037568>',
        '<:owoah:409342761595043850>',
        '<:sss:409342761662414848>' ]
    */

    var mainArr = []

    while(arr.length) {
          mainArr.push(arr.splice(0, 3).join(' '))
    }

    // Pretty printing array 
    // (This is the o/p which is specified in the question, here I forgot everything about 100 characters)
    console.log(JSON.stringify(mainArr, null, 4))
    /*
      [
          "<:cmd:409342761179938838> <:nobot:409342761246916610> <:haha:409342761272344578>",
          "<:rrrr:409342761431728139> <:aaa:409342761439854593> <:fff:409342761503031296>",
          "<:woah:409342761532391424> <:swon:409342761549037568> <:owoah:409342761595043850>",
          "<:sss:409342761662414848>"
      ]
    */

Finally look at the below code executed on **Node REPL** to understand few of the above basic statements.

    H:\RishikeshAgrawani\Projects\Stk>node
    >
    > var data = "<:cmd:409342761179938838> " +
    ...           "<:nobot:409342761246916610> " +
    ...           "<:haha:409342761272344578> " +
    ...           "<:rrrr:409342761431728139> " +
    ...           "<:aaa:409342761439854593> " +
    ...           "<:fff:409342761503031296> " +
    ...           "<:woah:409342761532391424> " +
    ...           "<:swon:409342761549037568> " +
    ...           "<:owoah:409342761595043850> "+
    ...           "<:sss:409342761662414848>"
    undefined
    >
    > arr
    [ '<:cmd:409342761179938838>',
      '<:nobot:409342761246916610>',
      '<:haha:409342761272344578>',
      '<:rrrr:409342761431728139>',
      '<:aaa:409342761439854593>',
      '<:fff:409342761503031296>',
      '<:woah:409342761532391424>',
      '<:swon:409342761549037568>',
      '<:owoah:409342761595043850>',
      '<:sss:409342761662414848>' ]
    >
    > arr[0]
    '<:cmd:409342761179938838>'
    > arr[0].length
    25
    >
    > arr[1].length
    27
    >
    > arr[2].length
    26
    >
    > arr[3].length
    26
    > arr[4].length
    25
    > arr[5].length
    25
    > arr[6].length
    26
    >
    > var mainArr = []
    undefined
    >
    > while(arr.length) {
    ...       mainArr.push(arr.splice(0, 3).join(' '))
    ... }
    4
    >
    > mainArr
    [ '<:cmd:409342761179938838> <:nobot:409342761246916610> <:haha:409342761272344578>',
      '<:rrrr:409342761431728139> <:aaa:409342761439854593> <:fff:409342761503031296>',
      '<:woah:409342761532391424> <:swon:409342761549037568> <:owoah:409342761595043850>',
      '<:sss:409342761662414848>' ]
    >
    > mainArr[0]
    '<:cmd:409342761179938838> <:nobot:409342761246916610> <:haha:409342761272344578>'
    >
    > mainArr[1]
    '<:rrrr:409342761431728139> <:aaa:409342761439854593> <:fff:409342761503031296>'
    >
    > mainArr[2]
    '<:woah:409342761532391424> <:swon:409342761549037568> <:owoah:409342761595043850>'
    >
    > mainArr[0].length
    80
    > mainArr[1].length
    78
    > mainArr[2].length
    81
    >

Thanks.