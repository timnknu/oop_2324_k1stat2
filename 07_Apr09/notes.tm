<TeXmacs|2.1.1>

<style|<tuple|generic|ukrainian>>

<\body>
  <\math>
    a<rsub|0>=\<cdots\>

    a<rsub|n>=f<around*|(|n,a<rsub|n-1>,<math-bf|p>|)>

    a<rsub|n>=f<around*|(|n,a<rsub|n-1>,a<rsub|n-2>,\<ldots\>,a<rsub|n-k>,<math-bf|p>|)>
  </math>

  \;

  ***

  <\math>
    lim<rsub|\<varepsilon\>\<rightarrow\>0><frac|<around*|(|1+\<varepsilon\>|)><rsup|p>-1|\<varepsilon\>>=p

    \;

    <around*|\||x|\|>\<less\>1

    <around*|(|1+x|)><rsup|n>=1+x\<cdummy\>n+\<cdots\>
  </math>

  \;

  ***

  \;

  <\math>
    a<rsub|0>=1

    a<rsub|n>=<frac|x<rsup|n>|n!>=f<around*|(|n,a<rsub|n-1>;<math-bf|p>|)>=a<rsub|n-1>\<cdummy\><frac|x|n>

    <frac|x<rsup|n>|n!>=<frac|x<rsup|n-1>\<cdummy\>x|<around*|(|n-1|)>!\<cdummy\>n>=<frac|x<rsup|n-1>|<around*|(|n-1|)>!>\<cdummy\><frac|x|n>

    \;
  </math>

  ***

  <\math>
    D<rsub|5>=<around*|\||<tabular|<tformat|<table|<row|<cell|b>|<cell|c>|<cell|0>|<cell|0>|<cell|0>>|<row|<cell|a>|<cell|b>|<cell|c>|<cell|0>|<cell|0>>|<row|<cell|0>|<cell|a>|<cell|b>|<cell|c>|<cell|0>>|<row|<cell|0>|<cell|0>|<cell|a>|<cell|b>|<cell|c>>|<row|<cell|0>|<cell|0>|<cell|0>|<cell|a>|<cell|b>>>>>|\|>=b\<cdummy\><around*|\||<tabular|<tformat|<table|<row|<cell|b>|<cell|c>|<cell|0>|<cell|0>>|<row|<cell|a>|<cell|b>|<cell|c>|<cell|0>>|<row|<cell|0>|<cell|a>|<cell|b>|<cell|c>>|<row|<cell|0>|<cell|0>|<cell|a>|<cell|b>>>>>|\|>-c\<cdummy\><around*|\||<tabular|<tformat|<table|<row|<cell|a>|<cell|c>|<cell|0>|<cell|0>>|<row|<cell|0>|<cell|b>|<cell|c>|<cell|0>>|<row|<cell|0>|<cell|a>|<cell|b>|<cell|c>>|<row|<cell|0>|<cell|0>|<cell|a>|<cell|b>>>>>|\|>=

    =b\<cdummy\>D<rsub|4>-c\<cdummy\><around*|\||<tabular|<tformat|<table|<row|<cell|a>|<cell|c>|<cell|0>|<cell|0>>|<row|<cell|0>|<cell|b>|<cell|c>|<cell|0>>|<row|<cell|0>|<cell|a>|<cell|b>|<cell|c>>|<row|<cell|0>|<cell|0>|<cell|a>|<cell|b>>>>>|\|>=b\<cdummy\>D<rsub|4>-c\<cdummy\>a\<cdummy\><around*|\||<tabular|<tformat|<table|<row|<cell|b>|<cell|c>|<cell|0>>|<row|<cell|a>|<cell|b>|<cell|c>>|<row|<cell|0>|<cell|a>|<cell|b>>>>>|\|>=b\<cdummy\>D<rsub|4>-c\<cdummy\>a\<cdummy\>D<rsub|3>

    D<rsub|1>=b

    D<rsub|2>=<around*|\||<tabular|<tformat|<table|<row|<cell|b>|<cell|c>>|<row|<cell|a>|<cell|b>>>>>|\|>=b<rsup|2>-a
    c
  </math>

  \;

  ***
</body>

<\initial>
  <\collection>
    <associate|font|roman>
    <associate|font-family|rm>
    <associate|math-font|roman>
    <associate|page-medium|paper>
  </collection>
</initial>