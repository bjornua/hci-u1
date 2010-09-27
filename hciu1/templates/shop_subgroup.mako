<%inherit file="/xhtml11.mako"/>
<h1>Vareoversigt</h1>
<p>Vælg en underkategori for at se vareoversigten.</p>
<ul id="categories">
<ul>
%for x in products:
<li><a href=${url_for("show_product", id=x[0])}>${escape(x[1])}</a></li>
%endfor
</ul>

