#include "logevent.h"
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSlider>

LogEvent::LogEvent(Entry *parent)
    : Entry(parent)
{
    QLineEdit *title = new QLineEdit(this);
    QLineEdit *category = new QLineEdit(this);
    QDateTimeEdit *startDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QDateTimeEdit *endDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QLineEdit *location = new QLineEdit(this);
    QSlider *mood = new QSlider(this);
    QSlider *spoons = new QSlider(this);

    this->frm->addRow("Title:", title);
    this->frm->addRow("Category:", category);
    this->frm->addRow("Start:", startDT);
    this->frm->addRow("End:", endDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Mood:", mood);
    this->frm->addRow("Spoons:", spoons);

    populate();
}
