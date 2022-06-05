Main |:
    <!> "Escriu el nombre d'elements:"
    <?> n
    llista <- {}
    Fib n llista
    <!> llista
:|

Fib n llista |:
    if n > 2 |:
        t1 <- 0
        t2 <- 1
        next <- t1 + t2
        <!> "Seqüència de Fibonacci de" n "elements"
        llista << t1
        llista << t2
        i <- 3
        while i <= n |:
            llista << next
            t1 <- t2
            t2 <- next
            next <- t1 + t2
            i <- i + 1
        :|
    :| else |:
        <!> "Escriu un nombre major de 2."
    :|
:|