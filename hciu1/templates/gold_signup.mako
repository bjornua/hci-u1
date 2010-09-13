<%inherit file="/xhtml11.mako"/>
<h1>Bliv medlem</h1>
<p>Du har valgt guld medlemskab, indtast følgende oplysninger for at fuldføre oprettelsen.</p>
<form action="${url_for("signup_complete")}">
    <dl>
    <dt><label for="name">Fulde navn</label></dt>
    <dd><input name="name" type="text" /></dd>
    </dl>
    <dl>
    <dt><label for="address">Adresse</label></dt>
    <dd><input name="address" type="text" /></dd>
    </dl>
    <dl>
    <dt><label for="postal_code">Postnr.</label></dt>
    <dd><input name="postal_code" type="text" /></dd>
    </dl>
    <dl>
    <dt><label for="city">By</label></dt>
    <dd><input name="city" type="text" /></dd>
    </dl>
    <dl>
    <dt><label for="phone">Telefonnr.</label></dt>
    <dd><input name="phone" type="text" /></dd>
    </dl>
    <dl>
    <dt><label for="mail">E-mail</label></dt>
    <dd><input name="mail" type="text" /></dd>
    </dl>
    <dl>
    <dt></dt>
    <dd><input name="submit" type="submit" value="Tilmeld" /></dd>
    </dl>
</form>
