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
# * File Name : pycrate_csn1dir/psi3_ter_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.21a Packet System Information Type 3 ter
# top-level object: PSI3 ter message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

rtd6_struct = CSN1Alt(name='rtd6_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='rtd', bit=6)])})

gprs_rep_priority_description_struct = CSN1List(name='gprs_rep_priority_description_struct', list=[
  CSN1Bit(name='number_cells', bit=7),
  CSN1Bit(name='rep_priority', num=([0], lambda x: x))])

rtd12_struct = CSN1Alt(name='rtd12_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='rtd', bit=12)])})

real_time_difference_description_struct = CSN1List(name='real_time_difference_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='cell_index_start_rtd', bit=7)])}),
    CSN1Ref(name='rtd_struct', obj=rtd6_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='0'),
      CSN1Ref(name='rtd_struct', obj=rtd6_struct)]),
    CSN1Val(name='', val='1')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='cell_index_start_rtd', bit=7)])}),
    CSN1Ref(name='rtd_struct', obj=rtd12_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='0'),
      CSN1Ref(name='rtd_struct', obj=rtd12_struct)]),
    CSN1Val(name='', val='1')])})])

psi3_ter_message_content = CSN1List(name='psi3_ter_message_content', trunc=True, list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Bit(name='psi3_change_mark', bit=2),
  CSN1Bit(name='psi3_ter_index', bit=4),
  CSN1Bit(name='psi3_ter_count', bit=4),
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='real_time_difference_description', obj=real_time_difference_description_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='gprs_rep_priority_description', obj=gprs_rep_priority_description_struct)])}),
    CSN1Ref(obj=padding_bits)])])

