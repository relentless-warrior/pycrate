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
# * File Name : pycrate_csn1dir/packet_si_status_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.17b Packet SI Status
# top-level object: Packet SI Status message content

# external references
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.padding_bits import padding_bits

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

si_message_list_struct = CSN1List(name='si_message_list_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='si_message_type', bit=8),
    CSN1Alt(alt={
      '00': ('mess_rec', [
      CSN1Val(name='', val='null')]),
      '01': ('mess_rec', [
      CSN1Val(name='', val='null')]),
      '10': ('mess_rec', [
      CSN1Bit(name='six_change_mark', bit=3),
      CSN1Bit(name='six_count', bit=4),
      CSN1Bit(name='instance_bitmap', bit=([2], lambda x: x + 1))]),
      '11': ('mess_rec', [
      CSN1Bit(name='six_change_mark', bit=3)])})]),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='additional_msg_type')])

unknown_si_message_list_struct = CSN1List(name='unknown_si_message_list_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='si_message_type', bit=8)]),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='additional_msg_type')])

packet_si_status_message_content = CSN1List(name='packet_si_status_message_content', list=[
  CSN1Ref(name='global_tfi', obj=global_tfi_ie),
  CSN1Bit(name='bcch_change_mark', bit=3),
  CSN1Ref(name='received_si_message_list', obj=si_message_list_struct),
  CSN1Ref(name='received_unknown_si_message_list', obj=unknown_si_message_list_struct),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Bit(name='pscsi_support'),
    CSN1Bit(name='ps_rel_req'),
    CSN1Ref(obj=padding_bits)]),
    None: ('', [])})])

