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
# * File Name : pycrate_csn1dir/ec_packet_power_control_timing_advance_message_content.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.55 EC Packet Power Control/Timing Advance
# top-level object: EC Packet Power Control/Timing Advance message content

# external references
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.ec_packet_timing_advance_ie import ec_packet_timing_advance_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.used_dl_coverage_class_ie import used_dl_coverage_class_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

ec_packet_power_control_timing_advance_message_content = CSN1List(name='ec_packet_power_control_timing_advance_message_content', list=[
  CSN1Ref(name='used_dl_coverage_class', obj=used_dl_coverage_class_ie),
  CSN1List(list=[
    CSN1Ref(name='global_tfi', obj=global_tfi_ie),
    CSN1List(list=[
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='t_avg_t', bit=5)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='ec_packet_timing_advance', obj=ec_packet_timing_advance_ie)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='gamma', bit=5)])}),
      CSN1Ref(obj=padding_bits)])])])

