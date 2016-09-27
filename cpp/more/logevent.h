#ifndef LOGEVENT_H
#define LOGEVENT_H

#include <QWidget>
#include "entry.h"

class LogEvent: public Entry {
public:
    // explicit
    LogEvent(QWindow *parent = 0);
    ~LogEvent(); // destructor
};


#endif // LOGEVENT_H
