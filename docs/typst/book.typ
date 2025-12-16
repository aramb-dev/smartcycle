#let title = "SmartCycle Book"
#let subtitle = "Consolidated Modules"
#let author = "SmartCycle Team"
#let date = datetime.today().display()

#set page(
  numbering: "1",
  margin: (x: 1.5cm, y: 2cm)
)
#set text(size: 11pt, font: "New Computer Modern")
#set par(justify: true)

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  text(size: 18pt, weight: "bold", it.body)
  v(0.5cm)
}

#show heading.where(level: 2): it => {
  v(0.3cm)
  text(size: 14pt, weight: "bold", it.body)
  v(0.2cm)
}

// Title page
#align(center)[
  #text(size: 24pt, weight: "bold")[#title]
  
  #v(0.5cm)
  #text(size: 14pt)[#subtitle]
  
  #v(2cm)
  #text(size: 12pt)[#author]
  
  #v(0.5cm)
  #text(size: 11pt)[#date]
]

#pagebreak()

// Table of Contents
#outline(indent: auto)

#pagebreak()

= Overview

#raw(read("../modules/overview.md"), lang: "markdown", block: true)

= Module 1

#raw(read("../../module1/README.md"), lang: "markdown", block: true)

== Plan

#raw(read("../../module1/plan.md"), lang: "markdown", block: true)

== Code: main.py

#raw(read("../../module1/main.py"), lang: "python", block: true)

= Module 2

== Plan

#raw(read("../../module2/plan.md"), lang: "markdown", block: true)

== Components

#raw(read("../../module2/components.py"), lang: "python", block: true)

== Error Codes

#raw(read("../../module2/error_codes.py"), lang: "python", block: true)

== Main Script

#raw(read("../../module2/main.py"), lang: "python", block: true)

= Module 3

== Troubleshooting Report

#raw(read("../../module3/troubleshooting_report.md"), lang: "markdown", block: true)

== Flowchart

_This file is an Excalidraw diagram (open separately): module3/flowchart.excalidraw_

= Module 4

#raw(read("../../module4/plan.md"), lang: "markdown", block: true)

= Module 5

#raw(read("../../module5/readme.md"), lang: "markdown", block: true)

= Module 6

#raw(read("../../module6/readme.md"), lang: "markdown", block: true)
