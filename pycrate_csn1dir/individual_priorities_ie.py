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
# * File Name : pycrate_csn1dir/individual_priorities_ie.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.50 Individual Priorities
# top-level object: Individual priorities IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

repeated_individual_utran_priority_parameters_struct = CSN1List(name='repeated_individual_utran_priority_parameters_struct', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='fdd_arfcn', bit=14)]),
    CSN1Val(name='', val='0')]),
    '1': ('', [
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='tdd_arfcn', bit=14)]),
    CSN1Val(name='', val='0')])}),
  CSN1Bit(name='utran_priority', bit=3)])

repeated_individual_e_utran_priority_parameters_struct = CSN1List(name='repeated_individual_e_utran_priority_parameters_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='earfcn', bit=16)]),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='e_utran_priority', bit=3)])

_3g_individual_priority_parameters_description_struct = CSN1List(name='_3g_individual_priority_parameters_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='default_utran_priority', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_individual_utran_priority_parameters', obj=repeated_individual_utran_priority_parameters_struct)]),
  CSN1Val(name='', val='0')])

e_utran_individual_priority_parameters_description_struct = CSN1List(name='e_utran_individual_priority_parameters_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='default_e_utran_priority', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_individual_e_utran_priority_parameters', obj=repeated_individual_e_utran_priority_parameters_struct)]),
  CSN1Val(name='', val='0')])

individual_priorities_ie = CSN1Alt(name='individual_priorities_ie', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='geran_priority', bit=3),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='_3g_individual_priority_parameters_description', obj=_3g_individual_priority_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='e_utran_individual_priority_parameters_description', obj=e_utran_individual_priority_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='t3230_timeout_value', bit=3)])})])})

