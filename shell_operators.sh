#!/bin/bash

echo "-------------------"
#1. piemers (merkis 2+2=4) -
# - gala rezultats simbolu rinda "2+2" nevis skaitlis 4
val=2+2
echo "Bez apostrofiem "$val

echo "-------------------"
#2. piemers  (merkis 2+2=4)
: <<'END'
val1=`expr 2+2`
echo "Neparasti apostrofi bez atstarpem  "$val1
val2='expr 2+2'
echo "Parasti apostrofi bez atstarpem " $val2
val3=`expr 2 + 2`
echo "Neparasti apostrofi ar atstarpem "$val3
val4='expr 2 + 2'
echo "Parasti apostrofi ar atstarpem "$val4
END

#3. piemers (+,-,*,/) 
#: <<'END'
val31=`expr 2 + 3`
echo "2 + 3 = "$val31
val32=`expr 2 - 3`
echo "2 - 3 = "$val32
val33=`expr 2 \* 3`
echo "2 * 3 = "$val33
val34=`expr 2 / 3`
echo "2 / 3 = "$val34
val35=`expr 5 % 3`
echo "2 % 3 = "$val35
#END
