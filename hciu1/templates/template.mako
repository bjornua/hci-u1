<%inherit file="/xhtml11.mako"/>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>HCI - U1</title>
    <link rel="stylesheet" href="/static/style.css" type="text/css" />
</head>
<body>
    <div id="main">
        <div id="top_banner">Pensionist <span id="dagger">&dagger;</span> Sagen</div>
        <div id="left_menu">
            <a href="${url_for("new_member")}">BLIV MEDLEM</a></div>
        <div id="content">
            ${next.body()}
        </div>
        <div id="right_menu">
            <a href="${url_for("shop")}">WEBSHOP</a>
        </div>

        <div id="bottom_banner">
            
        </div>
    </div>
</body>

