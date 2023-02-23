BAD_EMAIL = '''
    Received: from XXXXXXXXXX.namprd06.prod.outlook.com
    (1803:20b8:312:1-9::9)by XXXXXXXXXX.namprd06.prod.outlook.com
    with HTTPS; Thu, 23 Feb 202301:14:04 +0000\r\nReceived: from
    XXXXXXXXXXXX.namprd14.prod.outlook.com (1111:22222:5:19l::19)
    n d=communications.lifemiles.com;h=From:To:Subject:Date:List
    : 0\r\nX-EOPTenantAttributedMessage: 84df9e7f-e9f6-40af-b435-aa
    lEKzlldkEwenlQM0Ru?==?utf-8?B?ZXhJekpFSnBWRVdReG1odURVREZ3NVpY
    .lifemiles.com/?qs=0a659d55eb3bdc9c25e0767f9e8b3026e1e234a6882f94f81bd2e
    body/eight: auto !important;margin-left: auto !i
    html>; }.mobile-hidden { display:n !important; }logo { d
    </html>
    '''

MISSING_HTML_BODY_EMAIL = '''
    Received: from XXXXXXXXXX.namprd06.prod.outlook.com
    (1803:20b8:312:1-9::9)by XXXXXXXXXX.namprd06.prod.outlook.com
    with HTTPS; Thu, 23 Feb 202301:14:04 +0000\r\nReceived: from
    XXXXXXXXXXXX.namprd14.prod.outlook.com (1111:22222:5:19l::19)
    n d=communications.lifemiles.com;h=From:To:Subject:Date:List
    : 0\r\nX-EOPTenantAttributedMessage: 84df9e7f-e9f6-40af-b435-aa
    lEKzlldkEwenlQM0Ru?==?utf-8?B?ZXhJekpFSnBWRVdReG1odURVREZ3NVpY
    .lifemiles.com/?qs=0a659d55eb3bdc9c25e0767f9e8b3026e1e234a6882f94f81bd2e
    body/eight: auto !important;margin-left: auto !i
    html>; }.mobile-hidden { display:n !important; }logo { d
    </html>
    <html>
    some text
    </body>
    </html>
'''

GOOD_EMPTY_EMAIL = '''
    Received: from XXXXXXXXXX.namprd06.prod.outlook.com
    (1803:20b8:312:1-9::9)by XXXXXXXXXX.namprd06.prod.outlook.com
    with HTTPS; Thu, 23 Feb 202301:14:04 +0000\r\nReceived: from
    XXXXXXXXXXXX.namprd14.prod.outlook.com (1111:22222:5:19l::19)
    n d=communications.lifemiles.com;h=From:To:Subject:Date:List
    : 0\r\nX-EOPTenantAttributedMessage: 84df9e7f-e9f6-40af-b435-aa
    lEKzlldkEwenlQM0Ru?==?utf-8?B?ZXhJekpFSnBWRVdReG1odURVREZ3NVpY
    .lifemiles.com/?qs=0a659d55eb3bdc9c25e0767f9e8b3026e1e234a6882f94f81bd2e
    body/eight: auto !important;margin-left: auto !i
    html>; }.mobile-hidden { display:n !important; }logo { d
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
    <html><head>\r\n
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1,
    maximum-scale=1, user-scalable=0">\r\n
    <style type="text/css">ReadMsgBody{ width: 100%;}\r\n
    .ExternalClass {width: 100%;}.ExternalClass, .ExternalClass p,
    .ExternalClass span, .ExternalClass
    font, .ExternalClass td, .ExternalClass div {line-height: 100%;}\r\n
    body {-webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;
    margin:0 !important;}</style>
    </head>
    <body bgcolor="#ffffff" text="#000000" style="background-color: #ffffff;
    color: #000000; padding: 0px; -webkit-text-size-adjust:none;
    font-size: 16px; font-family:arial,helvetica,sans-serif;"></body></html>
    '''

INCOMPLETE_HTML_EMAIL = '''
    Received: from XXXXXXXXXX.namprd06.prod.outlook.com
    (1803:20b8:312:1-9::9)by XXXXXXXXXX.namprd06.prod.outlook.com
    with HTTPS; Thu, 23 Feb 202301:14:04 +0000\r\nReceived: from
    XXXXXXXXXXXX.namprd14.prod.outlook.com (1111:22222:5:19l::19)
    n d=communications.lifemiles.com;h=From:To:Subject:Date:List
    : 0\r\nX-EOPTenantAttributedMessage: 84df9e7f-e9f6-40af-b435-aa
    lEKzlldkEwenlQM0Ru?==?utf-8?B?ZXhJekpFSnBWRVdReG1odURVREZ3NVpY
    .lifemiles.com/?qs=0a659d55eb3bdc9c25e0767f9e8b3026e1e234a6882f94f81bd2e
    body/eight: auto !important;margin-left: auto !i
    html>; }.mobile-hidden { display:n !important; }logo { d
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
    <html><head>\r\n
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1,
    maximum-scale=1, user-scalable=0">\r\n
    <style type="text/css">ReadMsgBody{ width: 100%;}\r\n
    .ExternalClass {width: 100%;}.ExternalClass, .ExternalClass p,
    .ExternalClass span, .ExternalClass
    font, .ExternalClass td, .ExternalClass div {line-height: 100%;}\r\n
    body {-webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;
    margin:0 !important;}>
    </head>
    <body bgcolor="#ffffff" text="#000000" style="background-color: #ffffff;
    color: #000000; padding: 0px; -webkit-text-size-adjust:none;
    font-size: 16px; font-family:arial,helvetica,sans-serif;">
    <h1>Some header</h1>
    <div class="some-class" id="some-id">Some random content</div>
    <section>Some text for this section</section>
    <table><thead><th>Some column</th></thead><tbody><tr><td>Some content</td>
    </tr></tbody></table>
    <footer>
    Some footer
    </footer>
    </body>
    </html>
    '''

GOOD_FULL_EMAIL = '''
    Received: from XXXXXXXXXX.namprd06.prod.outlook.com
    (1803:20b8:312:1-9::9)by XXXXXXXXXX.namprd06.prod.outlook.com
    with HTTPS; Thu, 23 Feb 202301:14:04 +0000\r\nReceived: from
    XXXXXXXXXXXX.namprd14.prod.outlook.com (1111:22222:5:19l::19)
    n d=communications.lifemiles.com;h=From:To:Subject:Date:List
    : 0\r\nX-EOPTenantAttributedMessage: 84df9e7f-e9f6-40af-b435-aa
    lEKzlldkEwenlQM0Ru?==?utf-8?B?ZXhJekpFSnBWRVdReG1odURVREZ3NVpY
    .lifemiles.com/?qs=0a659d55eb3bdc9c25e0767f9e8b3026e1e234a6882f94f81bd2e
    body/eight: auto !important;margin-left: auto !i
    html>; }.mobile-hidden { display:n !important; }logo { d
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
    <html><head>\r\n
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1,
    maximum-scale=1, user-scalable=0">\r\n
    <style type="text/css">ReadMsgBody{ width: 100%;}\r\n
    .ExternalClass {width: 100%;}.ExternalClass, .ExternalClass p,
    .ExternalClass span, .ExternalClass
    font, .ExternalClass td, .ExternalClass div {line-height: 100%;}\r\n
    body {-webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;
    margin:0 !important;}</style>
    </head>
    <body bgcolor="#ffffff" text="#000000" style="background-color: #ffffff;
    color: #000000; padding: 0px; -webkit-text-size-adjust:none;
    font-size: 16px; font-family:arial,helvetica,sans-serif;">
    <h1>Some header</h1>
    <div class="some-class" id="some-id">Some random content</div>
    <section>Some text for this section</section>
    <table><thead><th>Some column</th></thead><tbody><tr><td>Some content</td>
    </tr></tbody></table>
    <footer>
    Some footer
    </footer>
    </body>
    </html>
    '''
