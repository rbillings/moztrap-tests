#!/usr/bin/env python
#
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Case Conductor
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Jonny Gerig Meyer <jonny@oddbird.net>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from base_page import CaseConductorBasePage
from datetime import datetime


class CaseConductorCreateRunPage(CaseConductorBasePage):

    _page_title = 'Mozilla Case Conductor'

    _name_locator = 'id=id_name'
    _cycle_select_locator = 'id=id_test_cycle'
    _description_locator = 'id=id_description'
    _start_date_locator = 'id=id_start_date'
    _end_date_locator = 'id=id_end_date'
    _submit_locator = 'css=#run-form .form-actions > button'
    _run_manage_locator = u'css=#manageruns .managelist article.item .title[title="%(run_name)s"]'
    _run_homepage_locator = u"css=.selectruns .finder .carousel .runs .colcontent .title:contains(%(run_name)s)"
    _run_tests_button_locator = u"css=.environment .form-actions button:contains(run tests in %(run_name)s!)"

    def go_to_create_run_page(self):
        self.selenium.open('/manage/testrun/add/')
        self.is_the_current_page

    def create_run(self, name='Test Run', cycle='Test Cycle', desc='This is a test run', start_date='2011-01-01', end_date='2012-12-31'):
        dt_string = datetime.utcnow().isoformat()
        run = {}
        run['name'] = u'%(name)s %(dt_string)s' % {'name': name, 'dt_string': dt_string}
        run['desc'] = u'%(desc)s created on %(dt_string)s' % {'desc': desc, 'dt_string': dt_string}
        run['manage_locator'] = self._run_manage_locator % {'run_name': run['name']}
        run['homepage_locator'] = self._run_homepage_locator % {'run_name': run['name']}
        run['run_tests_locator'] = self._run_tests_button_locator % {'run_name': run['name']}

        self.type(self._name_locator, run['name'])
        self.select(self._cycle_select_locator, cycle)
        self.type(self._description_locator, run['desc'])
        self.type(self._start_date_locator, start_date)
        self.type(self._end_date_locator, end_date)
        self.click(self._submit_locator, wait_flag=True)

        return run