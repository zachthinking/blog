# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For 个人
site_prefix = "/"
template = "Galileo"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": False,
    "repo": "zachthinking/write2024@gh-pages"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "扎克爱思的个人网站"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = ""
author = "扎克爱思"
email = "zach.thinking@gmail.com"
author_homepage = "https://zachthinking.github.io/"
description = "分享个人所思所得"
key_words = ["扎克爱思", "博客"]
language = 'chinese'
external_links = [
    {
        "name": "链接1",
        "url": "https://",
        "brief": ""
    }
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
        "name": "GitHub",
        "url": "https://github.com/zachthinking",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": False,
    "el": '#vcomments',
    "appId": "",
    "appKey": "",
    "visitor": False,
    "recordIP": False
}

head_addon = ''

footer_addon = ''

body_addon = ''
