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
# * File Name : pycrate_csn1dir/packet_enhanced_measurement_report_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.9d Packet Enhanced Measurement Report
# top-level object: PACKET ENHANCED MEASUREMENT REPORT message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.utran_csg_measurement_report_ie import utran_csg_measurement_report_ie
from pycrate_csn1dir.e_utran_csg_measurement_report_ie import e_utran_csg_measurement_report_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

serving_cell_data_struct = CSN1List(name='serving_cell_data_struct', list=[
  CSN1Bit(name='rxlev_serving_cell', bit=6),
  CSN1Val(name='', val='0')])

repeated_invalid_bsic_information_struct = CSN1List(name='repeated_invalid_bsic_information_struct', list=[
  CSN1Bit(name='bcch_freq_ncell', bit=5),
  CSN1Bit(name='bsic', bit=6),
  CSN1Bit(name='rxlev_ncell', bit=6)])

e_utran_measurement_report_struct = CSN1List(name='e_utran_measurement_report_struct', list=[
  CSN1Bit(name='n_e_utran', bit=2),
  CSN1List(num=([0], lambda x: x + 1), list=[
    CSN1Bit(name='e_utran_frequency_index', bit=3),
    CSN1Bit(name='cell_identity', bit=9),
    CSN1Bit(name='reporting_quantity', bit=6)])])

nc_measurement_report_struct = CSN1List(name='nc_measurement_report_struct', list=[
  CSN1Bit(name='nc_mode'),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='ba_used'),
    CSN1Bit(name='_3g_ba_used')]),
    '1': ('', [
    CSN1Bit(name='psi3_change_mark', bit=2)])}),
  CSN1Bit(name='pmo_used'),
  CSN1Bit(name='bsic_seen'),
  CSN1Bit(name='scale'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='serving_cell_data', obj=serving_cell_data_struct)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_invalid_bsic_information', obj=repeated_invalid_bsic_information_struct)]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(num=-1, alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='reporting_quantity', bit=6)])})])})])

packet_enhanced_measurement_report_message_content = CSN1List(name='packet_enhanced_measurement_report_message_content', list=[
  CSN1Bit(name='tlli_g_rnti', bit=32),
  CSN1Ref(name='nc_measurement_report', obj=nc_measurement_report_struct),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='g_rnti_extension', bit=4)])}),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Bit(name='bitmap_length', bit=7),
      CSN1Alt(num=([1], lambda x: x + 1), alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='reporting_quantity', bit=6)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='e_utran_measurement_report', obj=e_utran_measurement_report_struct)])}),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='utran_csg_measurement_report', obj=utran_csg_measurement_report_ie)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='e_utran_csg_measurement_report', obj=e_utran_csg_measurement_report_ie)])}),
        CSN1Alt(alt={
          '0': ('', [
          CSN1Bit(bit=-1)]),
          '1': ('', [
          CSN1Bit(name='si23_ba_used'),
          CSN1Ref(obj=padding_bits)]),
          None: ('', [])})]),
        None: ('', [])})]),
      None: ('', [])})]),
    None: ('', [])})])

