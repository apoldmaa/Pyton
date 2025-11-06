max_punktid = 100
eksami_tulemus = float(input("sisesta punktid "))
protsent = (eksami_tulemus / max_punktid) * 100
if protsent >= 90:
     hinne = 5
elif protsent >= 75:
    hinne = 4
elif protsent >= 50:
    hinne = 3
elif protsent >= 25:
    hinne = 2
else:
    hinne = 1

print(f"eksami_tulemus: {protsent:.1f}% ---> hinne {hinne}")