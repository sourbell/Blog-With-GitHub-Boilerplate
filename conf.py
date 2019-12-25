# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://project.sourbell.im/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "sourbell/project@gh-pages"
}

# 站点设置
site_name = "豪猪尾巴"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-24T23:19+08:00"
author = "Bristletail"
email = "i@sourbell.im"
author_homepage = "https://sourbell.im"
description = "Alive"
key_words = ['Maverick', 'sourbell', 'Bristletail', 'blog']
language = 'zh-CN'
background_img = '${static_prefix}bg/photo-1575892935016-d97e79254d93.jpg'
external_links = [
    # {
    #     "name": "Maverick",
    #     "url": "https://github.com/AlanDecode/Maverick",
    #     "brief": "🏄‍ Go My Own Way."
    # }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/sourbell",
        "icon": "gi fab fa-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/sourbell",
        "icon": "gi fab fa-github"
    },
    {
        "name": "Steam",
        "url": "https://steamcommunity.com/id/sourbell/",
        "icon": "gi fab fa-steam"
    },
    {
        "name": "PSN",
        "url": "https://my.playstation.com/profile/Bristle2tail",
        "icon": "gi fab fa-playstation"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<script src="https://kit.fontawesome.com/8780f0a025.js" crossorigin="anonymous"></script>
'''

footer_addon = ''

body_addon = ''
