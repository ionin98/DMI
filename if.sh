#!/bin/bash
#if (...) then ... else ...  fi
a=$1
if (( $a > 0 )); then
 echo "Galvenais zars (ja gadijuma), tad , kad $a>0"
elif (( $a == 0)); then
   echo "Alternat. zars (jā gad.), tad, kad $a ir =0"
else
   echo "Galvena zara (visi atlikusi gad.)"
   echo "Vai viennozimigs ne visiem iepr. jautajumiem"
fi
echo "Ši izdruka tiks veikta jebkura gadijuma"










#!/bin/bash

: <<"END"
#if (...) then ... else ...  fi
a=$1
if (( $a > 0 ))
then
   echo "Galvenais zars (jā gadijuma), tad, kad $a ir >0"
else
   echo "Galvena zara (ne gad.), tad, kad $a nav >0"
fi
echo "Ši izdruka tiks veikta jebkura gadijuma"
END










: <<'END'
#if (...) then ... fi
a=$1
if (( $a > 0 ))
then
   echo "Izdruka no galvena zara (jā gadijuma), tad, kad $a>0"
fi
echo "Ši izdruka tiks veikta jebkura gadijuma"
END
