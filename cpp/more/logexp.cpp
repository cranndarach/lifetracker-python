#include "logexp.h"
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSpinBox>

LogExp::LogExp(Entry *parent)
    : Entry(parent)
{
    QSpinBox *experience = new QSpinBox(this);
    QDateTimeEdit *whenDT = new QDateTimeEdit(QDateTime::currentDateTime());

    this->frm->addRow("EXP gained:", experience);
    this->frm->addRow("When:", whenDT);

    populate();
}

LogExp::~LogExp() {}
