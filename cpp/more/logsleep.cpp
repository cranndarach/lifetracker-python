#include "logsleep.h"
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSlider>

LogSleep::LogSleep(Entry *parent)
    : Entry(parent)
{
    QDateTimeEdit *sleepStartDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QDateTimeEdit *sleepEndDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QLineEdit *location = new QLineEdit(this);
    QSlider *quality = new QSlider(Qt::Horizontal, this);

    this->frm->addRow("Went to bed:", sleepStartDT);
    this->frm->addRow("Woke up:", sleepEndDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Quality:", quality);

    populate();
}

LogSleep::~LogSleep() {}
