<%inherit file="/xhtml11.mako"/>
<%
total_price = price * order_count

total_price = "%.2f" % (total_price/100)
total_price = total_price.replace(".",",")
total_price = total_price + " kr."
    
%>
<h1>Bekræft bestilling</h1>
<p>Bekræft venligst at du ønsker at betale <strong>${total_price}</strong> for 
${order_count} stk. ${escape(title)}.

<form action="${url_for("pay", id=id, method="POST")}" method="POST">
    <input type="submit" value="Bekræft bestilling!">
    <input type="hidden" name="total_price" value=${esc_attr(total_price)}>
</form>
