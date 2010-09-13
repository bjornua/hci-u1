<%inherit file="/xhtml11.mako"/>
<h1>Bliv medlem</h1>
<a href="${url_for("bronze_signup")}" id="bronze_link">
    <div id="bronze">
    <h2>Bronze (0%)</h2>
    <p>Som bronzemedlem, får du en masse fordele gratis.</p>
    </div>
</a>
<a href="${url_for("silver_signup")}" id="silver_link">
    <div id="silver">
    <h2>Sølv (5%)</h2>
    <p>Som sølvmedlem har du samme fordele som bronzemedlemmer, men herudover får du 5% rabat på alle dine køb. Medlemskabet koster 10 kr. om måneden.</p>
    </div>
</a>
<a href="${url_for("gold_signup")}" id="gold_link">
    <div id="gold">
    <h2>Guld (10%)</h2>
    <p>Som guldmedlem har du samme fordele som bronze- og sølvmedlemmer, her får du 10% rabat på alle dine køb. Medlemskabet koster 15 kr. om måneden.</p>
    </div>
</a>
