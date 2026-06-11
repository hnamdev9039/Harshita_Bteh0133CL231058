f = open("Report.txt","w")
f.write("name:rahul, marks:15")
f.write("name:ritesh,marks:33")
f.write("name:ravi, marks:36")
f.write("name:kashish, marks:68")
f.write("name:sonu, marks:78")

f.close()
print("file created")
f=open("Report.txt","r")
const=f.read()
if marks >45:
    print(const)
f.close()
