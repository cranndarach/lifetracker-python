#include "logevent.h"
#include <QLineEdit>
#include <QWidget>
#include <QDateTime>
#include <QSlider>

LogEvent::LogEvent(QWindow *parent):
    QWindow(parent)
{
    QLineEdit *title = new QLineEdit(this);
    QLineEdit *category = new QLineEdit(this);
    QDateTime *startDT = new QDateTime(this);
    QDateTime *endDT = new QDateTime(this);
    QLineEdit *location = new QLineEdit(this);
    QSlider *mood = new QSlider(this);
    QSlider *spoons = new QSlider(this);

    addLine("Title:", title);
    addLine("Category:", category);
    addLine("Start:", startDT);
    addLine("End:", endDT);
    addLine("Location:", location);
    addLine("Mood:", mood);
    addLine("Spoons:", spoons);

    populate();
}
