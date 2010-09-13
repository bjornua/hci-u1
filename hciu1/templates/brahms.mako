<%inherit file="/xhtml11.mako"/>
<h1>Violinkoncert (Brahms) af Event Shopping</h1>
<form action="${url_for("payment", product_id=1, method="POST")}" style="padding:0px 10px; border:1px dashed #000; margin:0 auto; width:150px; float:right;" method="POST">
    <h3>Køb billet</h3>
    <table style="width:150px">
        <tr>
            <td>Pr. stk.:</td><td>7,20 kr.</td>
        </tr><tr>
            <td style="width:60px;">Antal:</td><td><input id="order_count" name="order_count" style="width:100%;" type="text" value="1" size="2" /></td>
        </tr><tr>
            <td><strong>I alt:</strong></td><td id="total_price"><strong></strong></td>
        </tr><tr>
            <td colspan="2"><input type="submit" style="width:100%;" value="Køb billet"></td>
        </tr>
    </table>
</form>
<p>Koncerten er i Amager i Oktober 2010</p>
<p>Medlemspris: 2,7 kr. (normalpris: 3 kr.)</p>
<script type="text/javascript">
    function update_price(){
        total_price = $("#order_count").val() * 2.7;
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
