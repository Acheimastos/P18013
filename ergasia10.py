html_str = input("Write the url of the html page ")
f = open("%s.html" % (html_str), "r")
br = 0
p = 0
a = 0
lines = f.readlines()
for line in lines:
    line.split(" ")
    order_br = line.count("br>")
    order_p = line.count("<p>")
    order_a = line.count("<a")
    br = br + order_br
    p = p + order_p
    a = a + order_a
sunolo = br + p + a
print("<br> = %d  <p> = %d  <a> = %d  sunolo = %d ") % (br, p, a, sunolo)