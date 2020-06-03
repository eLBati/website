from odoo.http import request, Controller, route


class PWA(Controller):

    def get_asset_urls(self, asset_xml_id):
        qweb = request.env['ir.qweb'].sudo()
        assets = qweb._get_asset_nodes(asset_xml_id, {}, True, True)
        urls = []
        for asset in assets:
            if asset[0] == 'link':
                urls.append(asset[1]['href'])
            if asset[0] == 'script':
                urls.append(asset[1]['src'])
        return urls

    @route('/portal-service-worker.js', type='http', auth="public")
    def service_worker(self):
        qweb = request.env['ir.qweb'].sudo()
        urls = []
        urls.extend(self.get_asset_urls("web.assets_common"))
        urls.extend(self.get_asset_urls("web.assets_frontend"))
        version_list = []
        for url in urls:
            version_list.append(url.split('/')[3])
        cache_version = '-'.join(version_list)
        mimetype = 'text/javascript;charset=utf-8'
        content = qweb.render('portal_pwa.service_worker', {
            'pwa_cache_name': cache_version,
            'pwa_files_to_cache': urls,
        })
        return request.make_response(content, [('Content-Type', mimetype)])

    @route('/portal_pwa/manifest.json', type='http', auth="public")
    def manifest(self):
        qweb = request.env['ir.qweb'].sudo()
        config_param = request.env['ir.config_parameter'].sudo()
        pwa_name = config_param.get_param(
            "pwa.portal.manifest.name", "Odoo portal PWA")
        pwa_short_name = config_param.get_param(
            "pwa.portal.manifest.short_name", "Odoo portal PWA")
        icon128x128 = config_param.get_param(
            "pwa.portal.manifest.icon128x128",
            "/portal_pwa/static/img/icons/icon-128x128.png")
        icon144x144 = config_param.get_param(
            "pwa.portal.manifest.icon144x144",
            "/portal_pwa/static/img/icons/icon-144x144.png")
        icon152x152 = config_param.get_param(
            "pwa.portal.manifest.icon152x152",
            "/portal_pwa/static/img/icons/icon-152x152.png")
        icon192x192 = config_param.get_param(
            "pwa.portal.manifest.icon192x192",
            "/portal_pwa/static/img/icons/icon-192x192.png")
        icon256x256 = config_param.get_param(
            "pwa.portal.manifest.icon256x256",
            "/portal_pwa/static/img/icons/icon-256x256.png")
        icon512x512 = config_param.get_param(
            "pwa.portal.manifest.icon512x512",
            "/portal_pwa/static/img/icons/icon-512x512.png")
        background_color = config_param.get_param(
            "pwa.portal.manifest.background_color", "#2E69B5")
        theme_color = config_param.get_param(
            "pwa.portal.manifest.theme_color", "#2E69B5")
        mimetype = 'application/json;charset=utf-8'
        content = qweb.render('portal_pwa.manifest', {
            'pwa_name': pwa_name,
            'pwa_short_name': pwa_short_name,
            'icon128x128': icon128x128,
            'icon144x144': icon144x144,
            'icon152x152': icon152x152,
            'icon192x192': icon192x192,
            'icon256x256': icon256x256,
            'icon512x512': icon512x512,
            'background_color': background_color,
            'theme_color': theme_color,
        })
        return request.make_response(content, [('Content-Type', mimetype)])
