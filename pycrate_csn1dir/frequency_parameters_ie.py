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
# * File Name : pycrate_csn1dir/frequency_parameters_ie.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.8 Frequency Parameters
# top-level object: Frequency Parameters IE

# external references
from pycrate_csn1dir.gprs_mobile_allocation_ie import gprs_mobile_allocation_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

direct_encoding_2_struct = CSN1List(name='direct_encoding_2_struct', list=[
  CSN1Bit(name='maio', bit=6),
  CSN1Bit(name='hsn', bit=6),
  CSN1Bit(name='length_of_ma_frequency_list_contents', bit=4),
  CSN1Bit(name='ma_frequency_list_contents', bit=8, num=([2], lambda x: x + 3))])

indirect_encoding_struct = CSN1List(name='indirect_encoding_struct', list=[
  CSN1Bit(name='maio', bit=6),
  CSN1Bit(name='ma_number', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='change_mark_1', bit=2),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='change_mark_2', bit=2)])})])})])

direct_encoding_1_struct = CSN1List(name='direct_encoding_1_struct', list=[
  CSN1Bit(name='maio', bit=6),
  CSN1Ref(name='gprs_mobile_allocation', obj=gprs_mobile_allocation_ie)])

frequency_parameters_ie = CSN1List(name='frequency_parameters_ie', list=[
  CSN1Bit(name='tsc', bit=3),
  CSN1Alt(alt={
    '00': ('', [
    CSN1Bit(name='arfcn', bit=10)]),
    '01': ('', [
    CSN1Ref(name='indirect_encoding', obj=indirect_encoding_struct)]),
    '10': ('', [
    CSN1Ref(name='direct_encoding_1', obj=direct_encoding_1_struct)]),
    '11': ('', [
    CSN1Ref(name='direct_encoding_2', obj=direct_encoding_2_struct)])})])

