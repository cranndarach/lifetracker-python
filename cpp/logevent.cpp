#include "logevent.h"
#include "ui_logevent.h"

LogEvent::LogEvent(QWidget *parent) :
    QDialog(parent)
{
    setupUi(this);
}

LogEvent::~LogEvent() {}
