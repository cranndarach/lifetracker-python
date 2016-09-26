#-------------------------------------------------
#
# Project created by QtCreator 2016-09-23T21:56:20
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = formtest
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    logevent.cpp \
    entry.cpp

HEADERS  += mainwindow.h \
    logevent.h \
    entry.h

FORMS    += mainwindow.ui \
    logevent.ui
