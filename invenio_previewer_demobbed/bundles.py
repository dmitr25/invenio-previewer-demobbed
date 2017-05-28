# -*- coding: utf-8 -*-
#
# This file is part of Invenio-Previewer-Demobbed
# Copyright (C) 2017 CERN
#
# Invenio-Previewer-Demobbed is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio-Previewer-Demobbed is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio-Previewer-Demobbed; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Invenio-Previewer-Demobbed bundles."""

from invenio.ext.assets import Bundle


js = Bundle(
    "vendors/demobbed-viewer/js/lib/jquery.js",
    "vendors/demobbed-viewer/js/lib/d3.js",
    "vendors/demobbed-viewer/js/lib/three.js",
    "vendors/demobbed-viewer/js/lib/three3DExtras.min.js",

    "vendors/demobbed-viewer/js/DetCfg-def.js",
    "vendors/demobbed-viewer/js/Utils-def.js",
    "vendors/demobbed-viewer/js/Hits-defs.js",
    "vendors/demobbed-viewer/js/Vertex-def.js",
    "vendors/demobbed-viewer/js/TrackECC-def.js",
    "vendors/demobbed-viewer/js/Event-def.js",
    "vendors/demobbed-viewer/js/loadEvent.js",
    "vendors/demobbed-viewer/js/DetElems-defs.js",
    "vendors/demobbed-viewer/js/MgrGeomED-def.js",
    "vendors/demobbed-viewer/js/MgrDrawED-def.js",
    "vendors/demobbed-viewer/js/MgrDrawECC-def.js",
    "vendors/demobbed-viewer/js/Demobbed-def.js",
    "vendors/demobbed-viewer/js/init.js",
    "vendors/demobbed-viewer/js/Demobbed-fills.js",
    "vendors/demobbed-viewer/js/MgrGeomED-fills.js",
    "vendors/demobbed-viewer/js/MgrGeomED-funcAdd.js",
    "vendors/demobbed-viewer/js/MgrDrawED-funcAdd.js",
    "vendors/demobbed-viewer/js/MgrDrawECC-funcAdd.js",

    output="previewer_demobbed.js",
    filters="requirejs",
    weight=51,
    bower={
    "demobbed-viewer": "0.9.4-invenio.22"
    }
)

styles = Bundle(
    "vendors/demobbed-viewer/css/demobbed.css",
    output="previewer_demobbed.css",
    filters="cleancss",
    weight=51
)
