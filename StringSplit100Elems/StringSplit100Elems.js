ar data = "<:cmd:409342761179938838> " +
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