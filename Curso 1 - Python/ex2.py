seg = input("Por favor, entre com o número de segundos que deseja converter: ")
s = int(seg)

d = s // 86400
s2 = s % 86400

h = s2 // 3600
s3 = s2 % 3600

m = s3 // 60
s4 = s3 % 60

print(d, "dias,", h, "horas,", m,"minutos e", s4,"segundos")
