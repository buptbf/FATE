#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import numpy as np
from federatedml.feature.instance import Instance
from federatedml.feature.sparse_vector import SparseVector
from arch.api import session


class BaseFilterTest(object):
    def __init__(self):
        self.table_list = []
        self.guest_id = 9999
        self.host_id = 10000

    def tearDown(self):
        for table in self.table_list:
            table.destroy()
        print("Finish testing")