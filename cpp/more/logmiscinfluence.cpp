#include "logmiscinfluence.h"
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSlider>

LogMiscInfluence::LogMiscInfluence(Entry *parent)
    : Entry(parent)
{
    QLineEdit *title = new QLineEdit(this);
    QLineEdit *category = new QLineEdit(this);
    QDateTimeEdit *whenDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QLineEdit *location = new QLineEdit(this);
    QSlider *intensity = new QSlider(Qt::Horizontal, this);

    this->frm->addRow("Title:", title);
    this->frm->addRow("Category:", category);
    this->frm->addRow("When:", whenDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Intensity:", intensity);

    populate();
}

LogMiscInfluence::~LogMiscInfluence() {}
