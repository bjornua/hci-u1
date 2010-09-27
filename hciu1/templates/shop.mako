<%inherit file="/xhtml11.mako"/>
<h1>Vareoversigt</h1>
<p>Vælg en kategori for at se vareoversigten.</p>
<ul id="categories">
<ul>
%for x in groups:
<li><a href=${url_for("shop_group",group=x)}>${escape(x.title())}</a></li>
%endfor
</ul>

