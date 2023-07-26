>[!Important] Theorem
>## Master Theorem
> #masters_algo #masters_algorithm #masters_theorem
>
>$T(n) = aT(n/b) + f(n)$
>where we interpret $n/b$ to mean either $\lfloor n/b \rfloor$ or $\lceil n/b\rceil$. Then >$T(n)$ has the following asymptotic bounds:
>1. If $f(n) = O\left( n^{\log_{b }(x) - \in} \right)$ for some constant $\in \gt 0$, then $T(n) = \Theta \left( n^{\log_{b}(a)}\right)$.
>2. If $f(n) = \Theta (n^{\log_{b}a})$, then $T(n) = \Theta (n^{\log_{b}(a)} \ln(n))$.
>3. If $f(n) = \Omega (n^{\log_{b}a} + \in)$ for some constant $\in \gt 0$, and if $a f (n/b) \leq c f (n)$ for some constant $c \lt 1$ and all sufficient large $n$, then $T(n) = \Theta (f(n))$.


