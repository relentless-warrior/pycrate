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
# * File Name : pycrate_csn1dir/gprs_mobile_allocation_ie.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.10a GPRS Mobile Allocation
# top-level object: GPRS Mobile Allocation IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

rfl_number_list_struct = CSN1List(name='rfl_number_list_struct', list=[
  CSN1Bit(name='rfl_number', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1SelfRef()])})])

arfcn_index_list_struct = CSN1List(name='arfcn_index_list_struct', list=[
  CSN1Bit(name='arfcn_index', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1SelfRef()])})])

gprs_mobile_allocation_ie = CSN1List(name='gprs_mobile_allocation_ie', list=[
  CSN1Bit(name='hsn', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='rfl_number_list', obj=rfl_number_list_struct)])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='ma_length', bit=6),
    CSN1Bit(name='ma_bitmap', bit=([1], lambda x: x + 1))]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='arfcn_index_list', obj=arfcn_index_list_struct)])})])})])

