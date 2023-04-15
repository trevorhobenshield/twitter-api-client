\c 20 1000

/pe:{.[{if[(x+y+z)<0;'"Must be >= 0"];x+y+z};(x;y;z);{0N!x;0b}]}
/.Q.fc[f] z

t:("S ISS B  F";(,:)",")0:`:s.csv
/count t
meta t

show t:([]a:`foo`bar`baz;b:5 10 15f)
@[t;1 2;@[;`b;-[;4]]] /nest @ ?