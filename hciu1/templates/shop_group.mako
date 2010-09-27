<%inherit file="/xhtml11.mako"/>
<h1>Vareoversigt</h1>
<p>Vælg en underkategori for at se vareoversigten.</p>
<ul id="categories">
<ul>
%for x in subgroups:
<li><a href=${url_for("shop_subgroup",group=group, subgroup=x)}>${escape(x.title())}</a></li>
%endfor
</ul>

