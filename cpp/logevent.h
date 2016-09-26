#ifndef LOGEVENT_H
#define LOGEVENT_H

#include "ui_logevent.h"
#include <QDialog>

class LogEvent : public QDialog, public Entry, private Ui::LogEvent
{
    Q_OBJECT

public:
    explicit LogEvent(QWidget *parent = 0);
    ~LogEvent();
};

#endif // LOGEVENT_H
