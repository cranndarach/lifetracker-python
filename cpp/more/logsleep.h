#ifndef LOGSLEEP_H
#define LOGSLEEP_H

#include "entry.h"

class LogSleep: public Entry {
public:
    // explicit
    LogSleep(Entry *parent = 0);
    ~LogSleep(); // destructor
};


#endif // LOGSLEEP_H
