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
# * File Name : pycrate_csn1dir/egprs_packet_downlink_ack_nack_type_3_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.6f EGPRS Packet Downlink Ack/Nack Type 3
# top-level object: EGPRS Packet Downlink Ack/Nack Type 3 message content

# external references
from pycrate_csn1dir.extension_bits_ie import extension_bits_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.egprs_channel_quality_report_type_2_ie import egprs_channel_quality_report_type_2_ie
from pycrate_csn1dir.egprs_ack_nack_description_ie import egprs_ack_nack_description_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

egprs_packet_downlink_ack_nack_type_3_message_content = CSN1List(name='egprs_packet_downlink_ack_nack_type_3_message_content', trunc=True, list=[
  CSN1Bit(name='downlink_tfi', bit=5),
  CSN1Bit(name='ms_out_of_memory'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_quality_report', obj=egprs_channel_quality_report_type_2_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='secondary_dual_carrier_channel_report', obj=egprs_channel_quality_report_type_2_ie)])}),
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='extension_bits', obj=extension_bits_ie)])}),
    CSN1Ref(name='egprs_ack_nack_description', obj=egprs_ack_nack_description_ie)]),
  CSN1Ref(obj=padding_bits)])

