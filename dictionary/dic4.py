'''ques4-suppose there are two dictionary called boys and girls containing names as key and ages as values.write a program to merge two 
dictionary  into third dictionary'''
boys={'nilesh':41,'soumitra':42,'nadeem':47}
girls={'rasika':38,'rajashree0':43,'rasika':44}
combined={**boys,**girls}
print(combined)
combined={**girls,**boys}
print(combined)