Main |:
    <!> "Escriu el nombre d'elements:"
    <?> n
    Fib n
:|

Fib n |:
    if n > 2 |:
        t1 <- 0
        t2 <- 1
        next <- t1 + t2
        <!> "Seqüència de Fibonacci de" n "elements"
        <!> t1
        <!> t2
        i <- 3
        while i <= n |:
            <!> next
            t1 <- t2
            t2 <- next
            next <- t1 + t2
            i <- i + 1
        :|
    :| else |:
        <!> "Escriu un nombre major de 2."
    :|
:|