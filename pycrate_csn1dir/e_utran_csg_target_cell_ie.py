# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/e_utran_csg_target_cell_ie.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.62 E-UTRAN CSG Target cell
# top-level object: E-UTRAN CSG Target cell IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

plmn_id_struct = CSN1List(name='plmn_id_struct', list=[
  CSN1Bit(name='mcc', bit=12),
  CSN1Bit(name='mnc', bit=12)])

e_utran_csg_target_cell_ie = CSN1List(name='e_utran_csg_target_cell_ie', list=[
  CSN1Bit(name='e_utran_ci', bit=28),
  CSN1Bit(name='tracking_area_code', bit=16),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='plmn_id', obj=plmn_id_struct)])})])

