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
# * File Name : pycrate_csn1dir/si_22_rest_octets.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37n SI 22 Rest Octets
# top-level object: SI 22 Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

network_sharing_information_struct = CSN1List(name='network_sharing_information_struct', list=[
  CSN1Bit(name='si23_indicator'),
  CSN1Bit(name='common_plmn_allowed'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='common_plmn_ps_acc', bit=16)])}),
  CSN1Bit(name='nb_additional_plmns', bit=2),
  CSN1List(num=([3], lambda x: x + 1), list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mcc', bit=12)])}),
    CSN1Bit(name='mnc', bit=12),
    CSN1Bit(name='ncc_permitted', bit=8),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='additional_acc', bit=16)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='ps_acc', bit=16)])})])})])])

si_22_rest_octets = CSN1List(name='si_22_rest_octets', list=[
  CSN1Bit(name='si_22_change_mark', bit=2),
  CSN1Bit(name='si_22_index', bit=3),
  CSN1Bit(name='si_22_count', bit=3),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='network_sharing_information', obj=network_sharing_information_struct)])}),
  CSN1Ref(obj=spare_padding)])

