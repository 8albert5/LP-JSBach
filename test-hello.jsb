~~~ Kleines Program in JSBach ~~~

Main |:
    <!> "Hallo Bach"
    <!> ori "->" dst
    <:> nota
    <:> {}
    <:> {A}
    <:> {F8}
    HanoiRec (n - 1) src aux dst
    HanoiRec #src src dst aux
    note <- src[#src]
    note <- {}
    note <- {A}
    note <- {A B C}
    8< src[#src]
    dst << note
    <:> {A B C}
:|