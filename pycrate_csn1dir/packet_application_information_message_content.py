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
# * File Name : pycrate_csn1dir/packet_application_information_message_content.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.47 Packet Application Information
# top-level object: Packet Application Information message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

packet_application_information_message_content = CSN1List(name='packet_application_information_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1List(list=[
    CSN1Bit(name='application_type', bit=4),
    CSN1Bit(name='application_data', bit=8, num=-1),
    CSN1Ref(obj=padding_bits)])])

