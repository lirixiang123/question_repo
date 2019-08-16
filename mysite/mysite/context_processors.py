from . import settings
def site_info(request):
    #站点信息

    site = {}
    # site["SITE_URL"] = settings.SITE_URL
    site["SITE_NAME"] = settings.SITE_NAME
    site["SITE_DESC"] = settings.SITE_DESC
    site["KEYWORDS"]=settings.SITE_KEYWORDS
    # site["PRO_GIT"] = settings.PRO_GIT
    # site["PRO_RSS"] = settings.PRO_RSS
    # site["WEIBO_URL"] = settings.WEIBO_URL

    return locals()