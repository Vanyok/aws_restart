diction = {
	"one" : "first",
	"two" : "second",
	"three": "third",
	"four" : "forth"
}
i=0
for item in diction:
	i += 1
	if i == 3:
		print(item)
print(diction)