https://stackoverflow.com/questions/10561923/unicodedecodeerror-ascii-codec-cant-decode-byte-0xef-in-position-1

It's fine to use the below code in the top of your script.

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

But I will suggest you to also add `# -*- coding: utf-8 -*` line at very top of the script.

Omitting it throws below error in my case when I try to execute `basic.py`.

```bash
$ python basic.py
  File "01_basic.py", line 14
SyntaxError: Non-ASCII character '\xd9' in file basic.py on line 14, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```


The following is the code present in `basic.py` which throws above error.

    from pylatex import Document, Section, Subsection, Command, Package
    from pylatex.utils import italic, NoEscape

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def fill_document(doc):
        with doc.create(Section('ِش سثؤفهخى')):
            doc.append('إخع ساخعمي شمصشغس سحثشن فاث فقعفا')
            doc.append(italic('فشمهؤ ؤخىفثىفس شقث شمسخ ىهؤث'))

            with doc.create(Subsection('آثص ٍعلاسثؤفهخى')):
                doc.append('بشةخعس ؤقشئغ ؤاشقشؤفثقس: $&#{}')


    if __name__ == '__main__':
        # Basic document
        doc = Document('basic')
        fill_document(doc)

Then I added `# -*- coding: utf-8 -*-` line at very top and executed. It worked.

    # -*- coding: utf-8 -*-
    from pylatex import Document, Section, Subsection, Command, Package
    from pylatex.utils import italic, NoEscape

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def fill_document(doc):
        with doc.create(Section('ِش سثؤفهخى')):
            doc.append('إخع ساخعمي شمصشغس سحثشن فاث فقعفا')
            doc.append(italic('فشمهؤ ؤخىفثىفس شقث شمسخ ىهؤث'))

            with doc.create(Subsection('آثص ٍعلاسثؤفهخى')):
                doc.append('بشةخعس ؤقشئغ ؤاشقشؤفثقس: $&#{}')


    if __name__ == '__main__':
        # Basic document
        doc = Document('basic')
        fill_document(doc)

Thanks.