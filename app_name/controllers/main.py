# -*- coding: utf-8 -*-
from odoo import api, http
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.modules import get_module_resource
from odoo.http import request
from datetime import datetime
import calendar, math, re, io, base64, os, json, werkzeug

import logging
_logger = logging.getLogger(__name__)


class MainController(http.Controller):

    @http.route([
        '/web/quaint_starter/function_name',
        '/quaint_starter/function_name',
    ], methods=['POST', 'GET'], type='http', auth="none", website=True, csrf=False, cors="*")
    def function_name(self, dbname=None, **kw):
        _logger.info("==========testing...==========")
        response = True
        return response

