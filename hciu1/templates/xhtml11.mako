<?xml version="1.0" encoding="UTF-8"?>
<%
    response.mimetype="text/html"
    response.charset = "utf-8"
%><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>HCI - U1</title>
    <link media="screen" rel="stylesheet" type="text/css" href="/static/screen.css"/>
</head>
<body>
<div id="main">
<div id="top_banner"><a href="${url_for("index")}">Pensionist <span id="dagger">&dagger;</span> Sagen</a></div>
<div id="left_menu"><a href="${url_for("signup")}">Klik her for at blive medlem</a></div>
<div id="content">
    ${next.body()}
</div>
<div id="right_menu"><a href="${url_for("shop")}">Klik her for at komme til webbutikken</a></div>

<div id="bottom_banner"></div>
</div>
</body>
</html>
