#!/usr/bin/python
# -*- coding: utf-8 -*-

# shell 'ā
# echo "Lietotaj, ludzu, ievadi kaut ko: "
# read a
# python''ā
# print "Lietotaj, ludzu, ievadi kaut ko: "
# a = input()

'''
a = input("Lietotaj, ludzu, ievadi kaut ko: ")
print "Tu ievadiji lielumu ar %s dat tipu"%(type(a))
print a * a
print a + a
a = raw_input("Lietotaj, ludzu, ievadi kaut ko: ")
print "Tu ievadiji lielumu ar %s dat tipu"%(type(a))
#print a * a
print a + a
'''


a = raw_input("Lietotaj, ludzu ievadi savu vardu: ")
b = raw_input("Lietotaj, ludzu ievadi savu uzvardu: ")
print "Tatad, Tevi sauc - %s"%(a + ' ' + b)
print "Tatad, Tevi sauc - %s"%(a + chr(32) + b)
