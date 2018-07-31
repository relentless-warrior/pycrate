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
# * File Name : pycrate_csn1dir/ec_system_information_type_3.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.43r EC System information type 3
# top-level object: EC System Information Type 3



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

ec_cell_reselection_parameters_struct = CSN1List(name='ec_cell_reselection_parameters_struct', list=[
  CSN1Bit(name='cell_reselect_hysteresis', bit=3),
  CSN1Bit(name='cell_reselect_offset', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='c1_delta_min', bit=2),
    CSN1Bit(name='c1_delta_max', bit=3)])})])

ec_neighbour_cell_description_struct = CSN1List(name='ec_neighbour_cell_description_struct', list=[
  CSN1Bit(name='numberofoctets', bit=5),
  CSN1Bit(name='neighbour_frequency_list_information', bit=([0], lambda x: 8 * (x + 1)))])

ec_neighbour_cell_reselection_parameters_struct = CSN1List(name='ec_neighbour_cell_reselection_parameters_struct', list=[
  CSN1Bit(name='nb_ncell', bit=5),
  CSN1List(num=([0], lambda x: x + 1), list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(name='bsic', bit=6)]),
        '1': ('', [
        CSN1Bit(name='bsic', bit=9)])})])}),
    CSN1Bit(name='cell_type'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='cell_bar_access'),
        CSN1Bit(name='same_ra_as_serving_cell')])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='ec_rxlev_access_min', bit=6),
        CSN1Bit(name='ms_txpwr_max_cch', bit=5)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='cell_reselect_offset', bit=6)])})])})])])

ec_system_information_type_3 = CSN1List(name='ec_system_information_type_3', list=[
  CSN1Bit(name='message_type', bit=3),
  CSN1Bit(name='ec_si_3_index', bit=2),
  CSN1Bit(name='ec_si_3_count', bit=2),
  CSN1Bit(name='ec_si_change_mark', bit=5),
  CSN1Bit(name='ec_si_4_indicator'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ec_cell_reselection_parameters', obj=ec_cell_reselection_parameters_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ec_neighbour_cell_description', obj=ec_neighbour_cell_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ec_neighbour_cell_reselection_parameters', obj=ec_neighbour_cell_reselection_parameters_struct)])}),
  CSN1Ref(obj=spare_padding)])

