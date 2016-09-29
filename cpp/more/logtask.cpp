#include "logtask.h"
#include <QLineEdit>
#include <QDateTime>
#include <QDateTimeEdit>
#include <QSlider>
#include <QSpinBox>

LogTask::LogTask(Entry *parent)
    : Entry(parent)
{
    QLineEdit *title = new QLineEdit(this);
    QLineEdit *category = new QLineEdit(this);
    QDateTimeEdit *startDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QDateTimeEdit *endDT = new QDateTimeEdit(QDateTime::currentDateTime());
    QLineEdit *location = new QLineEdit(this);
    QSlider *mood = new QSlider(Qt::Horizontal, this);
    QSlider *spoons = new QSlider(Qt::Horizontal, this);
    QSlider *size = new QSlider(Qt::Horizontal, this);
    QSlider *progress = new QSlider(Qt::Horizontal, this);
    QSlider *quality = new QSlider(Qt::Horizontal, this);
    QSpinBox *experience = new QSpinBox(this);

    this->frm->addRow("Title:", title);
    this->frm->addRow("Category:", category);
    this->frm->addRow("Start:", startDT);
    this->frm->addRow("End:", endDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Mood:", mood);
    this->frm->addRow("Spoons:", spoons);
    this->frm->addRow("Size of task:", size);
    this->frm->addRow("Progress/completion:", progress);
    this->frm->addRow("Satisfaction/quality:", quality);
    this->frm->addRow("EXP gained:", experience);

    populate();
}

LogTask::~LogTask() {}
