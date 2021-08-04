# -*- coding: utf-8 -*-
"""Wrapper to run myapp from the command line.

:copyright: Copyright (c) 2017 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function
from pykern import pksubprocess
from pykern.pkcollections import PKDict
from pykern.pkdebug import pkdp, pkdc, pkdlog
from sirepo import simulation_db
from sirepo.template import template_common
import rsprivate.template.code1 as template
import sys


_SCHEMA = simulation_db.get_schema(template.SIM_TYPE)


def run(cfg_dir):
    pksubprocess.check_call_with_signals(
        [sys.executable, template_common.PARAMETERS_PYTHON_FILE],
    )
    template_common.write_sequential_result(PKDict(foo='bar'))
