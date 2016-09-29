#ifndef LOGEVENT_H
#define LOGEVENT_H

#include "entry.h"

class LogEvent: public Entry {
public:
    // explicit
    LogEvent(Entry *parent = 0);
    ~LogEvent(); // destructor
};


#endif // LOGEVENT_H
