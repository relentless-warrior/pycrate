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
# * File Name : pycrate_csn1dir/si16_rest_octets.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37e SI 16 Rest Octets
# top-level object: SI16 Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

lsa_identity = CSN1Alt(name='lsa_identity', alt={
  '0': ('', [
  CSN1Bit(name='lsa_id', bit=24)]),
  '1': ('', [
  CSN1Bit(name='shortlsa_id', bit=10)])})

lsa_id_information = CSN1List(name='lsa_id_information', list=[
  CSN1Ref(obj=lsa_identity),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1SelfRef()])})])

lsa_parameters = CSN1List(name='lsa_parameters', list=[
  CSN1Bit(name='prio_thr', bit=3),
  CSN1Bit(name='lsa_offset', bit=3),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mcc', bit=12),
    CSN1Bit(name='mnc', bit=12)])}),
  CSN1Ref(obj=lsa_id_information)])

si16_rest_octets = CSN1List(name='si16_rest_octets', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=lsa_parameters)]),
    'L': ('', [])}),
  CSN1Ref(obj=spare_padding)])

si17_rest_octets = CSN1Ref(name='si17_rest_octets', obj=si16_rest_octets)

