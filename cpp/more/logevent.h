#ifndef LOGEVENT_H
#define LOGEVENT_H

#include "entry.h"
#include <QObject>
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSlider>

class LogEvent: public Entry {
Q_OBJECT

public:
    LogEvent(Entry *parent = 0);
    void serialize();
    ~LogEvent(); // destructor

private:
    QLineEdit *title = new QLineEdit(this);
    QLineEdit *category = new QLineEdit(this);
    QDateTimeEdit *startDT = new QDateTimeEdit(QDateTime::currentDateTime(), this);
    QDateTimeEdit *endDT = new QDateTimeEdit(QDateTime::currentDateTime(), this);
    QLineEdit *location = new QLineEdit(this);
    QSlider *mood = new QSlider(Qt::Horizontal, this);
    QSlider *spoons = new QSlider(Qt::Horizontal, this);
};

#endif // LOGEVENT_H
