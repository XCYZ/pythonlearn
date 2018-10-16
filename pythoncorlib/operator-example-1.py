import operator
sequence = 1, 2, 4
print ("add", "=>", reduce(operator.add, sequence),
"sub", "=>", reduce(operator.sub, sequence),"\n",
"mul", "=>", reduce(operator.mul, sequence),"\n",
"concat", "=>", operator.concat("spam", "egg"),"\n",
"repeat", "=>", operator.repeat("spam", 5),"\n",
"getitem", "=>", operator.getitem(sequence, 2),"\n",
"indexOf", "=>", operator.indexOf(sequence, 2),"\n",
"sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3))

