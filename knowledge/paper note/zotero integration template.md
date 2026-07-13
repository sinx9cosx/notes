---
Title: "{{title}}"
ShortTitle: "{{shortTitle}}"
Author: "{{authors}}"
Date: '{% if date %}{{date | format("YYYY-MM")}}{% endif %}'
Publication: "{{publicationTitle}}"
Citekey: "{{citekey}}"
Rate: '{{allTags | length - (allTags | replace("🐱", "") | length)}}'
---

PDF:{{pdfZoteroLink | replace("select", "open-pdf")}}
#research/papers , {{hashTags  | replace("##", '#') | replace("#","#research/")}}
{% persist "annotations" %}
{% if isFirstImport %}
## Abstract
{{abstractNote}}
## Motivation
What's the motivation, key method and contribution?
## Result
How's the experiment done? How's the result?
## Method
What's the detailed method?
## Thinking
What did you learn? What doubts do you have?
## Annotations
{% endif %}{% set newAnnotations = annotations | filterby("date","dateafter", lastImportDate) %}{% if newAnnotations.length > 0 %}
#### Imported: {{importDate | format("YYYY-MM-DD h:mm a")}}
{% for a in newAnnotations %}
{% if a.annotatedText %}> {{a.annotatedText}} [Page{{a.page}}]({{a.attachment.select | replace("select", "open-pdf")}}?page={{a.page}}).
{% endif %}{% if a.comment %}> {{a.comment}}
{% endif %}{% if a.type == "image" %}> ![Page{{a.page}}]({{a.attachment.select | replace("select", "open-pdf")}}?page={{a.page}})
[[{{a.imageBaseName}}]]
{% endif %}{% endfor %}
{% endif %}{% endpersist %}
