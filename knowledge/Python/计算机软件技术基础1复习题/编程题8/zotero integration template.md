---
Title:"{{title}}"
ShortTitle:"{{shortTitle}}"
Author: "{{authors}}"
Date:'{% if date %}{{date | format("YYYY-MM")}}{% endif %}'
Publication:"{{publicationTitle}}"
Citekey: "{{citekey}}"
Rate:'{{allTags | length - (allTags | replace(""，"")) | length}}'
---


PDF:((pdfZoteroLink replace("select", "open-pdf")>
 research/papers , fhashTags  replace(  ", ' ', I replace(井"
"#research/")》
(% persist "annotations" %7
(% if isFirstlmport %7
## Abstract
((abstractNote))
## Motivation
What's the motivation, key method and contribution?

## Result
How's the experiment done? How's the result?
## Method
What's the detailed method?
## Thinking
What did you learn? What doubts do you have?
## Annotations
(% endif %/% set newAnnotations = annotations | filterby("date", "dateafter", lastlmportDate) %)(% if newAnnotations. length > 0 %#### Imported: KimportDate I format("YYYY-MM-DD h:mm a")》
(% for a in newAnnotations %)
(% if a.annotated Text %)> la.annotatedText) [Page(a, page)l(ta.atta
chment.select replace"select", "open-pdf))2page=(lapage)
(% endif %)(% if a.comment %7> (fa.comment)
(% endif %)(% if a.type == "image" %%> [Page(a.pagel(fa.attachm ent.select replace("select", "open-pdf')3page=fa,page)))!
[[la.imageBaseName]
(% endif %/(% endfor %)
(% endif %(% endpersist %
