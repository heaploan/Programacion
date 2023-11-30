secPerDay = 43200 
sec = int(input())
actalDay = (sec // (2 * secPerDay)) + 1
isMorning = (actalDay % 2) == 1 
if isMorning:
    momentDay = "mati"
else:
    momentDay = "nit"
time = f"{momentDay} del dia {actalDay}"
print(time)
