<%inherit file="/xhtml11.mako"/>
<%
if product_id == 1:
    price = 2.7
    product_name = "Billet til Violinkoncert (Brahms) af Event Shopping"
elif product_id == 2:
    price = 7.2
    product_name = "Die Forelle (Schubert) af Hostrup Musik"    


total_price = price * order_count

total_price = "%.2f" % total_price
total_price = total_price.replace(".",",")
total_price = total_price + " kr."
    
%>
<h1>Bekræft betaling</h1>
<p>Bekræft venligst at du ønsker at betale <strong>${total_price}</strong> for 
${order_count} stk. ${product_name}.

<form action="${url_for("pay", method="POST")}" method="POST">
    <input type="submit" value="Bekræft betaling!">
</form>
