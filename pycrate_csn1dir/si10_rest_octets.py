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
# * File Name : pycrate_csn1dir/si10_rest_octets.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.44 SI10 rest octets $(ASCI)$
# top-level object: SI10 rest octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

next_frequency = CSN1Val(name='next_frequency', val='H')

la_different = CSN1Alt(name='la_different', alt={
  'H': ('', [
  CSN1Bit(name='cell_reselect_hysteresis', bit=3)]),
  'L': ('', [])})

further_diff_cell_info = CSN1List(name='further_diff_cell_info', list=[
  CSN1Ref(obj=la_different),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='ms_txpwr_max_cch', bit=5)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='rxlev_access_min', bit=6)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='cell_reselect_offset', bit=6)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='temporary_offset', bit=3)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='penalty_time', bit=5)]),
    'L': ('', [])})])

diff_cell_pars = CSN1Alt(name='diff_cell_pars', alt={
  'H': ('cell_barred', []),
  'L': ('', [
  CSN1Ref(obj=further_diff_cell_info)])})

differential_cell_info = CSN1List(name='differential_cell_info', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='bcc', bit=3)]),
    'L': ('', [
    CSN1Bit(name='bsic', bit=6)])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=diff_cell_pars)]),
    'L': ('', [])})])

further_cell_info = CSN1List(name='further_cell_info', list=[
  CSN1Ref(obj=la_different),
  CSN1Bit(name='ms_txpwr_max_cch', bit=5),
  CSN1Bit(name='rxlev_access_min', bit=6),
  CSN1Bit(name='cell_reselect_offset', bit=6),
  CSN1Bit(name='temporary_offset', bit=3),
  CSN1Bit(name='penalty_time', bit=5)])

info_field = CSN1List(name='info_field', list=[
  CSN1Ref(obj=next_frequency, num=-1),
  CSN1Val(name='', val='L'),
  CSN1Ref(obj=differential_cell_info)])

cell_parameters = CSN1Alt(name='cell_parameters', alt={
  'H': ('cell_barred', []),
  'L': ('', [
  CSN1Ref(obj=further_cell_info)])})

cell_info = CSN1List(name='cell_info', list=[
  CSN1Bit(name='bsic', bit=6),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=cell_parameters)]),
    'L': ('', [])})])

neighbour_information = CSN1List(name='neighbour_information', list=[
  CSN1Bit(name='first_frequency', bit=5),
  CSN1Ref(obj=cell_info),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='H'),
    CSN1Ref(obj=info_field)]),
  CSN1Val(name='', val='L'),
  CSN1Ref(obj=spare_padding)])

si10_rest_octets = CSN1List(name='si10_rest_octets', list=[
  CSN1Bit(name='ba_ind'),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=neighbour_information)]),
    'L': ('', [
    CSN1Ref(obj=spare_padding)])})])

