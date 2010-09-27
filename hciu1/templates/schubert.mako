<%inherit file="/xhtml11.mako"/>
<%
    price_kr = price / 100
    price_string = ("%.2f" % price_kr).replace(".",",") + " kr."
%>
<h1>${title}</h1>
<form action="${url_for("payment", id=id, method="POST")}" style="padding:0px 10px; border:1px dashed #000; margin:0 auto; width:150px; float:right;" method="POST">
    <h3>Køb billet</h3>
    <table style="width:150px">
        <tr>
            <td>Pr. stk.:</td><td>${price_string}</td>
        </tr><tr>
            <td style="width:60px;">Antal:</td><td><input id="order_count" name="order_count" style="width:100%;" type="text" value="1" size="2" /></td>
        </tr><tr>
            <td><strong>I alt:</strong></td><td id="total_price"><strong></strong></td>
        </tr><tr>
            <td colspan="2"><input type="submit" style="width:100%;" value="Køb billet"></td>
        </tr>
    </table>
</form>
%if date != None:
<p>Dato:  ${date}</p>
%endif
<p>Medlemspris: ??? kr. (normalpris ${price_string})</p>
<script type="text/javascript">
    function update_price(){
        total_price = $("#order_count").val() * ${str(price_kr)};
        if(isNaN(total_price)){return};
        total_price = total_price.toFixed(2);
        total_price = String(total_price);
        total_price = total_price.replace(".",",") + " kr.";
        $("#total_price > strong").text(total_price);
    }
    update_price();
    $("#order_count").change(update_price);
    $("#order_count").keydown(update_price);
    $("#order_count").keyup(update_price);
    $("#order_count").keydown(update_price);
</script>
